(function(){
	'use strict';

	angular.module('rentApp')
		.config(['$routeProvider', config])
		.run(['$http', run]);

	function config($routeProvider) {
		$routeProvider
			.when('/', {
				templateUrl: '/static/partials/frontpage.html',
				controller: 'homeController'
			})
			.when('/store', {
				templateUrl: '/static/partials/catalog.html',
				controller: 'filmsController'
			})
			.when('/login', {
				templateUrl: '/static/partials/login.html',
				controller: 'loginController'
			})
			.when('/registration', {
				templateUrl: '/static/partials/registration.html',
				controller: 'registrationController'
			})
			.otherwise('/')
	}
	function run($http) {
		$http.defaults.xsrfHeaderName = 'X-CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';
	}
})();