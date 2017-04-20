var app= angular.module("contractapp", ['ngRoute','ds.clock','chart.js']);

angular.module('app', []).directive('setFocusIf', function() {
  return function link($scope, $element, $attr) {
    $scope.$watch($attr.setFocusIf, function(value) {
      if (value) { $element[0].focus(); }
    });
  };
});
app.config(['$httpProvider',function($httpProvider){
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}]);

