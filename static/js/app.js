'use strict';   // See note about 'use strict'; below

var myApp = angular.module('myApp', ['ngRoute',]);

myApp.controller('MainController', function($scope, $http) {
    $scope.response = "";

    $scope.submit = function() {
        console.log($scope.searchPhrase);
        $http.get("/search/" + $scope.searchPhrase).then(function(response) {
            $scope.response = response.data;
        }, function(err) {
            console.error(err);
            $scope.response = "Error";
        });
    };
});
