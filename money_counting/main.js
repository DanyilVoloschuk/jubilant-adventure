var app = angular.module('app', [])

app.controller('secondCtrl', function ($scope, myFactory) {
	$scope.myFactory = myFactory
	$scope.myFactory.list = [{thisname: 'Mario', thisprice: 23, thistype: 'clothes'}]	
	$scope._name = ''
	$scope.price = ''
	
	$scope.types = [
		{nm: 'clothes'},
		{nm: 'subscribes'},
		{nm: 'food'}	
	]
	
	$scope.add = function (a, b, c='') {
		if (!a || !b) return		
		$scope._name = ''
		$scope.price = ''
		$scope.myFactory.list.push({thisname: a, thisprice: b, thistype: c})
		console.log(a, b, $scope.myFactory.list)
	}	
})

app.controller('firstCtrl', function ($scope, myFactory) {
	$scope.myFactory = myFactory
})


app.factory('myFactory', function () {
	return{
		hello: function () { return 'hello world' }	
	}
})