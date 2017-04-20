// mytaskcontroller
app.controller("contractappcontroller",['$scope','$http',function($scope,$http){
// $scope.starttime = function(){
//     debugger;
//     var data = {
//             method: 'POST',
//             url: '/gettime',
//             data: {
                
//             }
//         }
//         $http(data)
//         .success(function (data) {
//             // alert(data);
//         }).error(function (data) {
//             // alert(data)
//         })
// }
// $scope.labels = ["Download Sales", "In-Store Sales", "Mail-Order Sales"];
// $scope.data = [300, 100, 100];


$scope.createpscclick = function(){
    debugger;
    var data = {
        method : 'POST',
        url : '/contractapp/createpsc/',
        data: {
            'txtcDate':$scope.txtcDate,
            'txtCExdate':$scope.txtCExdate,
            'txtCacntno':$scope.txtCacntno,
            'psctype':$scope.ddlPscType,
            'ddlCustomerid': $scope.ddlCustomerid,
            'txtCcustidname': $scope.txtCcustidname,
            'ddlsystems': $scope.ddlsystems,
            'txtMailingAddress': $scope.txtMailingAddress,
            'txtSummary': $scope.txtSummary,
            'txtIntrod': $scope.txtIntrod,
            'txtCProgrammingServices': $scope.txtCProgrammingServices,
            'txtCSummaryofWork': $scope.txtCSummaryofWork,
            'txtCDetailsofWork': $scope.txtCDetailsofWork,
            'txtCExpectedResults': $scope.txtCExpectedResults,
            'txtScheduleTime': $scope.txtScheduleTime,
            'txtTerms': $scope.txtTerms,
            'txtJobCompletion': $scope.txtJobCompletion,
            'txtCancellation': $scope.txtCancellation,
            'txtSchTimeChanges': $scope.txtSchTimeChanges,
            'txtTravelCosts': $scope.txtTravelCosts,
            'txtLiability': $scope.txtLiability,
            'txtClosing': $scope.txtClosing,
            'editor1': $scope.editor1,
            'txtHrsCEstimate': $scope.txtHrsCEstimate,
            'txtCHrlyRate': $scope.txtCHrlyRate,
            'txtCTotalEstimate': $scope.txtCTotalEstimate,
            'txtCDeposit': $scope.txtCDeposit,
            'txtWebSubId': $scope.txtWebSubId,
            'txtJobNo': $scope.txtJobNo,
            'rbtnPrintList': $scope.rbtnPrintList,
            // 'my-file-selector1': $scope.my-file-selector1,
            // 'my-file-selector2': $scope.my-file-selector2

        }
    }
     $http(data)
            .success(function (data){
                // alert('Data saved successfully.')
            }).error(function(data){
                //
            })
}
}]);