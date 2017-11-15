(function() {
	'use strict';
	angular.module('rentApp')
		.directive('filmCard', ['Login', 'moment', CardDirective]);

	function CardDirective(Login) {
		return {
			templateUrl: '/static/partials/film.html',
			restrict: 'E',
			controller: ['$scope', '$http', '$timeout', 'Login', function($scope, $http, $timeout, Login){
				var url = '/api/films/' + $scope.film.id + '/';
				var currentUser = Login.currentUser().id;

				$scope.currentDate = new Date().getTime();
				$scope.currentUser = currentUser;
				$scope.overdueCost = ($scope.film.cost + ($scope.film.cost * 0.05));
				
				Date.prototype.addDays = function(days) {
				  var dat = new Date(this.valueOf());
				  dat.setDate(dat.getDate() + days);
				  return dat;
				}

				var dat = new Date();

				$scope.compareDates = function(date1, date2) {
				   var dateObj1 = new Date(date1).getTime();
				   var dateObj2 = new Date(date2).getTime();

				   return (dateObj1 > dateObj2);
				}

				$scope.update = function($index) {
					console.log($index)
					console.log($scope.data[$index].status)
					$timeout(function(){
						$scope.data[$index].status = 'r';
						$scope.data[$index].due_back = dat.addDays(14);
						$scope.data[$index].borrower = currentUser
						$http.put(
							url,
							$scope.film
						)
					}, 400)
				};

				$scope.deposit = function($index) {
					$timeout(function(){
						$scope.data[$index].status = 'a';
						$scope.data[$index].due_back = null;
						$scope.data[$index].borrower = null;
						$http.put(
							url,
							$scope.film
						)
					}, 400)
				}

			}]
		};
	}
}());	