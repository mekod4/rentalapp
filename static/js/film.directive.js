(function() {
	'use strict';

	angular.module('rentApp')
		.directive('filmCard', CardDirective);

	function CardDirective() {
		return {
			templateUrl: '/static/partials/film.html',
			restrict: 'E',
			controller: ['$scope', '$http', '$timeout', function($scope, $http, $timeout){
				var url = '/api/films/' + $scope.film.id + '/';

				$scope.update = function($index) {
					console.log($index)
					console.log($scope.data[$index].status)
					$timeout(function(){
						$scope.data[$index].status = 'r';
						$http.put(
							url,
							$scope.film
						)
					}, 400)
				};

			}]
		};
	}
}());	