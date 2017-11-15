(function(){
	'use strict';

	angular
		.module('rentApp')
		.controller('homeController', 
			['$scope', '$location', '$http', HomeController])

	function HomeController($scope, $location, $http) {
        $scope.go = function(path) {
        	$location.path(path);
        }

        $scope.loginUrl = 'login';
	}
})();