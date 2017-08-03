
var expect = require('expect.js');

var pythreejs = require('../../src');

var services = require('@jupyterlab/services/lib');

var mngr = require('./testwidgetmanager');


function executeResult(future) {
    return new Promise(function(resolve, reject) {
        function hook(msg) {
            if (msg['msg_type'] === 'execute_result') {
                resolve(msg);
                future.removeMessageHook(hook);
            }
            return true;
        }
        future.registerMessageHook(hook);
    });
}

describe('# python back-propagation', () => {

    it('should back-propagate object hierarchy', () => {
        var kernel;
        var manager;
        var geometry;
        var material;
        var parent;
        return services.Kernel.startNew().then(value => {
            kernel = value;
            return kernel.ready;
        }).then(() => {

            manager = new mngr.WidgetManager(kernel);
            var future = kernel.requestExecute({
                code: 'import pythreejs\ntest_group = pythreejs.Group()\ntest_group.model_id'
            });
            return executeResult(future);
        }).then((result) => {

            var model_id = result.content['data']['text/plain'];
            // Remove quotes:
            model_id = model_id.slice(1, model_id.length-1);
            return manager.get_model(model_id);
        }).then((model) => {

            parent = model;
            expect(parent).to.not.be(undefined);
            // Create sphere + material with default values
            geometry = pythreejs.SphereGeometryModel.createJSSide(manager);
            material = pythreejs.MeshBasicMaterialModel.createJSSide(manager);
            return Promise.all([geometry, material]);
        }).then((values) => {

            geometry = values[0];
            material = values[1];
            return Promise.all([geometry.initPromise, material.initPromise]);
        }).then(() => {

            state = {
                geometry: geometry.serialize(geometry.get_state(true)),
                material: material.serialize(material.get_state(true)),
            };
            return pythreejs.MeshModel.createJSSide(manager, state);
        }).then((mesh) => {

            parent.obj.children.push(mesh.obj);
            parent.syncToModel(true);
            // FIXME: Return promise to wait for sync to complete
        }).then((result) => {

            var future = kernel.requestExecute({
                code: 'len(test_group.children)'
            });
            return executeResult(future);
        }).then((result) => {

            var length = result.content['data']['text/plain'];
            // Remove quotes:
            length = parseInt(length);
            expect(length).to.equal(1);
        }).then(() => {

            return kernel.shutdown();
        });
    });

});
