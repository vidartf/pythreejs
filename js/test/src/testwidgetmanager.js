
var _ = require('underscore');
var widgets = require("@jupyter-widgets/base");
var services = require('@jupyterlab/services/lib');

var pythreejs = require('../../src');



function WidgetManager(kernel) {
    widgets.ManagerBase.apply(this);

    this.kernel = kernel;
    kernel.registerCommTarget(this.comm_target_name,
        (comm, msg) => {
            let oldComm = new widgets.shims.services.Comm(comm);
            this.handle_comm_open(oldComm, msg);
    });

    this._awaiting_models = {};
}
_.extend(WidgetManager.prototype, widgets.ManagerBase.prototype, {
    display_view: function() {},

    loadClass(className, moduleName, moduleVersion) {
        if (moduleName === "@jupyter-widgets/base") {
            return Promise.resolve(widgets[className]);
        } else if (moduleName == "jupyter-threejs") {
            return Promise.resolve(pythreejs[className]);
        } else {
            return Promise.reject('Class ' + className + ' not found in module ' + moduleName);
        }
    },

    get_model(model_id) {
        var model = this._models[model_id];
        if (model !== undefined) {
            return model;
        }
        // Create new promise, that waits for widget to be created
        var promise = new Promise((resolve) => {
            this._awaiting_models[model_id] = resolve;
        }).then((value) => {
            return value;
        });
        return promise;
    },

    new_model(options, serialized_state = {}) {
        var model_id;
        if (options.model_id) {
            model_id = options.model_id;
        } else if (options.comm) {
            model_id = options.model_id = options.comm.comm_id;
        } else {
            throw new Error('Neither comm nor model_id provided in options object. At least one must exist.');
        }

        var modelPromise = this._make_model(options, serialized_state);
        this._models[model_id] = modelPromise;
        var awaitPromise = this._awaiting_models[model_id];
        if (awaitPromise) {
            delete this._awaiting_models[model_id];
            awaitPromise(modelPromise);
        }
        return modelPromise;
    },

    /**
     * Create a comm.
     */
    _create_comm(target_name, model_id, data, metadata) {
        let comm = this.kernel.connectToComm(target_name, model_id);
        if (data || metadata) {
            comm.open(data, metadata);
        }
        return Promise.resolve(new widgets.shims.services.Comm(comm));
    },

    /**
     * Get the currently-registered comms.
     */
    _get_comm_info() {
        return this.kernel.requestCommInfo({target: this.comm_target_name}).then(reply => reply.content.comms);
    }

});

exports.WidgetManager = WidgetManager;
