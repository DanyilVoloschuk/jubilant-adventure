var app = angular.module('app', [])

app.controller('secondCtrl', function ($scope, myFactory) {
	$scope.myFactory = myFactory
	$scope.myFactory.list = [{thisname: 'Mario', thisprice: 23, thistype: 'clothes'}]	
	$scope._name = ''
	$scope.price = ''
	$scope.types = [
		{nm: 'clothes'},
		{nm: 'subscribes'},
		{nm: 'food'},
		{nm: 'transport'},
		{nm: 'smth else'}	
	]
	$scope.myFactory.types = $scope.types
	
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
	$scope.current_list = ''
	$scope.current_list = $scope.myFactory.list
	
	$scope.sortList = function (sorting) {
		if (sorting){
			var a = []
			for (let i = 0; i < $scope.myFactory.list.length; i++)
				if ($scope.myFactory.list[i] == sorting)
					a.push($scope.myFactory.list[i])
			$scope.current_list = a
		}
	}
})


app.factory('myFactory', function () {
	return{
		hello: function () { return 'hello world' }	
	}
})