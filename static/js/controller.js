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

// $scope.submit = function(){
//     var fd = new FormData();
//     datas = $("#FormId").serializeArray();
//     // send other data in the form
//     for( var i = 0; i < datas.length; i++ ) {
//          fd.append(datas[i].name, datas[i].value);
//         };
//     // append file to FormData
//     fd.append("select_file", $("#id_select_file")[0].files[0])
//     // for sending manual values
//     fd.append("type", "edit");
//     url = "getter/test/",
//     $http.post(url, fd, {
//         headers: {'Content-Type': undefined },
//         transformRequest: angular.identity
//     }).success(function(data, status, headers, config) {
//         // this callback will be called asynchronously
//         // when the response is available
//     }).
//     error(function(data, status, headers, config) {
//         // called asynchronously if an error occurs
//         // or server returns response with an error status.
//         });
// };

$scope.createpscclick = function(){
    debugger;
    var data = {
        method : 'POST',
        url : '/contractapp/createpsc_save/',
        data : {
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
            'file1': $("#my-file-selector")[0].files[0]
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

$scope.custtomer_saveclick = function(){
    var data = {
        method: 'POST',
        url : '/contractapp/customer_save/',
        data :{
            'txt_first_name' : $scope.txt_first_name,
            'txt_last_name' : $scope.txt_last_name,
            'txt_address' : $scope.txt_address,
            'txt_mobile' : $scope.txt_mobile
        }
    }
    $http(data)
        .success(function (data){
            alert('Data saved successfully.')
        }).error(function(data){
            alert('Error.')
        })
}

$scope.emp_saveclick = function(){
    debugger;
    var data = {
        method: 'POST',
        url : '/contractapp/employee_save/',
        data :{
            'txt_emp_fname' : $scope.txt_emp_fname,
            'txt_emp_lname' : $scope.txt_emp_lname,
            'txt_emp_email' : $scope.txt_emp_email,
            'txt_emp_pwd' : $scope.txt_emp_pwd,
            'chk_isadmin' : $scope.chk_isadmin,
            'rdo_emp_status': $('#rdo_emp_status').val()
        }
    }
    $http(data)
        .success(function (data){
            alert('Data saved successfully.')
        }).error(function(data){
            alert('Error.')
        })
}

}]);