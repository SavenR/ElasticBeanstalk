app.controller('mainController', function($http){
    var mc = this;

    // template API connection to /slugs
    $http.get('/app')
    .then(function(data){
        console.log('connected to api')
        console.log(data);
        mc.items = data;
    })

});
