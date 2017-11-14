(function() {
    'use strict';

    angular.module('rentApp', [])
        .controller('filmsController',
            [ '$scope', '$http', FilmsController ]);

    function FilmsController($scope, $http) {
        $scope.add = function (list, title) {
            var card = {
                title: title
            };

            list.cards.push(card);
        };
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