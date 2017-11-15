(function() {
    'use strict';

    angular.module('rentApp', ['ngRoute'])
        .controller('filmsController',
            [ '$scope', '$http', '$location', 'Login', FilmsController ]);

    function FilmsController($scope, $http, $location, Login) {

        if (localStorage['currentUser']) {
            var currentUser = Login.currentUser().id;
        }
        $scope.currentUser = currentUser;

        $scope.homeLogged = function(){
            if (Login.isLoggedIn()) {
                return true;
                console.log('true')
            } else  {
                return false;
                console.log('false')
            }
        }

        $scope.go = function(path) {
            $location.path(path);
        }      
        
        $scope.logged = function(){
            if (Login.isLoggedIn()) {
                return true
            } else if (!Login.isLoggedIn()) {
                return false;
            }
        }
        $scope.logout = function(){
            delete localStorage.currentUser;
            $http.get('/auth/logout/')
                .then(function(){
                    $location.url('/login')
                });
        }

        $scope.data = [];

        $http.get('/api/films').then(
            function(response){
              $scope.data = response.data;
              console.log(response.data)
            }
        );

    }


}());