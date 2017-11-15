(function() {
    'use strict';

    angular.module('rentApp', ['ngRoute'])
        .controller('filmsController',
            [ '$scope', '$http', '$location', 'Login', FilmsController ]);

    function FilmsController($scope, $http, $location, Login) {
        $scope.add = function (list, title) {
            var card = {
                title: title
            };

            list.cards.push(card);
        };
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
        Login.redirectIfNotLoggedIn();
        console.log('klk')
        $scope.data = [];


        $http.get('/api/films').then(
            function(response){
              $scope.data = response.data;
              console.log(response.data)
            }
        );

    }


}());