(function() {
	'use strict';

	angular.module('rentApp')
		.directive('filmCard', CardDirective);

	function CardDirective() {
		return {
			templateUrl: '/static/partials/film.html',
			restrict: 'E',
			controller: ['$scope', '$http', function($scope, $http){
				var url = '/api/films/' + $scope.film.id + '/';
				$scope.update = function() {
					$http.put(
						url,
						$scope.film.status = 'r'
					);
				};
			}]
		};
	}
}());	