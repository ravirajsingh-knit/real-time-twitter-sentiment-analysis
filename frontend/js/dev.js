//var app=angular.module('sentiment',[]);


var app=angular.module("sentiment",["ngRoute"]);
app.config(function($routeProvider){
 //console.log("adjk")   
 $routeProvider.when("/home",{
                    templateUrl:"pages/intro.html",
                    //controller:'introCtrl'
                })
                .when("/",{
                    templateUrl:"pages/intro.html",
                    //controller: 'mod1Ctrl'
                })
                .when("/mod1",{
                    templateUrl:"pages/mod1.html",
                    controller: "mod1Ctrl"
                })
                .when("/mod2",{
                    templateUrl:"pages/mod2.html",
                    controller: 'mod2Ctrl'
                })
                .when("/mod3",{
                    templateUrl:"pages/mod3.html",
                    controller: 'mod3Ctrl'
                })
                .when("/mod4",{
                    templateUrl:"pages/mod4.html",
                    controller: 'mod4Ctrl'
                })
                .when("/mod5",{
                    templateUrl:"pages/mod5.html",
                    //controller: 'mod5Ctrl'
                })
                .otherwise("/home");
    
});



app.controller("mod1Ctrl",function($scope,$http){
    $scope.name="LOADING";
    $scope.detail="LOADING";
    $scope.link="LINKING";
    $scope.datas="";
    //$scope.category=['ALL'];
    $scope.info=[];
    $scope.info.push();
    $scope.info.push("HERE YOU CAN GET SENTIMENT FROM TWITTER ABOUT FAMOUS PEOPLE");   
    var url="https://telepathy.pythonanywhere.com/all";
    $http({
    method: 'GET',
    url: url
    })
    .then(function(response) {
        //First function handles success
       // alert("hello");
        $scope.datas = eval(response.data);
        $scope.category=[];
        $scope.category.push($scope.datas[0].category);
        for(var i=1;i<$scope.datas.length;i++)
            if($scope.category[$scope.category.length-1]!=$scope.datas[i].category)
                $scope.category.push($scope.datas[i].category);
       // alert($scope.category);
    }, function(response) {
        $scope.content = "Something went wrong";
    });






    $scope.load=function(data) {
       // alert("hhgxg");
        console.log(data.id);
        var id=data.id
        var url="https://telepathy.pythonanywhere.com/id/"+id.toString();
        //console.log(url);
        var xmlhttp = new XMLHttpRequest();
        //var url = "myTutorials.txt";
        //alert(url);

        xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $scope.info = eval(this.responseText);
         //   alert(JSON.stringify(this.responseText));
            
         }
        };
        xmlhttp.open("GET", url, false);
        xmlhttp.send();
        var imageParent = document.getElementById("img");
        imageParent.src = "/img/"+$scope.info[2];
        //alert(JSON.stringify($scope.info));
        var adddiv = document.getElementById("rts");

        adddiv.innerHTML = '';
        var iframe = document.createElement('iframe');
        iframe.height="500";
        iframe.width="1000";
        iframe.src = "http://telepathy.pythonanywhere.com/rts/"+id.toString();
        //adddiv.appendChild(h);
        adddiv.appendChild(iframe);

        var adddiv1 = document.getElementById("pie");
        adddiv1.innerHTML = '';
        var iframe1 = document.createElement('iframe');  
        iframe1.height="400";
        iframe1.width="650";
        iframe1.src = "http://telepathy.pythonanywhere.com/pie/"+id.toString();
        adddiv1.appendChild(iframe1);

        var play1 = document.getElementById('play1');
        play1.innerHTML = '';
        var h2 = document.createElement('h2');
        h2.textContent="REAL TIME TWITTER SENTIMENT ANALYSIS :";
        play1.appendChild(h2);



        var play2 = document.getElementById('play2');
        play2.innerHTML = '';
        var h1 = document.createElement('h2');
        h1.textContent="OVERALL SENTIMENT ANALYSIS :";
        play2.appendChild(h1);

    };

});


app.controller('mod2Ctrl',function($scope,$http) {
    // body...
    var url="https://telepath.pythonanywhere.com/all";
    var xmlhttp = new XMLHttpRequest();
        //var url = "myTutorials.txt";
        //alert(url);

        xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $scope.trends = eval(this.responseText);
         //   alert(JSON.stringify(this.responseText));
            
         }
        };
        xmlhttp.open("GET", url, false);
        xmlhttp.send();
        //console.log($scope.trends);


})
;
app.controller('mod3Ctrl',function($scope,$http){
    var url="https://telepath.pythonanywhere.com/all";
    var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $scope.trends = eval(this.responseText);
         //   alert(JSON.stringify(this.responseText));
            
         }
        };

        xmlhttp.open("GET", url, false);
        xmlhttp.send();
        
        $scope.load=function(data) {
            console.log(data.id);
            var id=data.id
            var adddiv = document.getElementById("rts");
            adddiv.innerHTML = '';
            var iframe = document.createElement('iframe');  
            iframe.height="500";
            iframe.width="1000";
            iframe.src = "http://telepath.pythonanywhere.com/rts/"+id.toString();
            adddiv.appendChild(iframe);

            var adddiv1 = document.getElementById("pie");
            adddiv1.innerHTML = '';
            var iframe1 = document.createElement('iframe');  
            iframe1.height="400";
            iframe1.width="650";
            iframe1.src = "http://telepath.pythonanywhere.com/pie/"+id.toString();
            adddiv1.appendChild(iframe1);
            //alert(id.toString());    

            var play1 = document.getElementById('play1');
            play1.innerHTML = '';
            var h2 = document.createElement('h2');
            h2.textContent="REAL TIME TWITTER SENTIMENT ANALYSIS :";
            play1.appendChild(h2);



            var play2 = document.getElementById('play2');
            play2.innerHTML = '';
            var h1 = document.createElement('h2');
            h1.textContent="OVERALL SENTIMENT ANALYSIS :";
            play2.appendChild(h1);
        }

        
});


app.controller('mod4Ctrl', function($scope,$http) {
    var url="https://telepathy.pythonanywhere.com/alltrends";
    $http({
    method: 'GET',
    url: url
    })
    .then(function(response) {
        //First function handles success
       // alert("hello");
        console.log(eval(response.data));
        $scope.trends = eval(response.data);
        $scope.country=[];
        $scope.country.push($scope.trends[0].name);
        for(var i=1;i<$scope.trends.length&&$scope.trends.length!=$scope.country.length-1;i++)
            if($scope.country[$scope.country.length-1]!=$scope.trends[i].country)
                $scope.country.push($scope.trends[i].country);
        //alert($scope.country);
    }, function(response) {
        $scope.content = "Something went wrong";
    });

    $scope.loadplay=function(data) {
       // alert("hhgxg");
        //console.log(data.id);
        var id=data.id;
        $scope.pname="";


        for(var i=1;i<$scope.trends.length;i++)
            if($scope.trends[i].id==id){
                var nmp=$scope.trends[i].name,temp="";
                var woeid=$scope.trends[i].woeid;
                for(var j=0;j<nmp.length;j++){
                    if(nmp.charCodeAt(j)<91&&nmp.charCodeAt(j)>64)
                        temp=temp+String.fromCharCode(nmp.charCodeAt(j)-65+97);
                    else if(nmp[j]=='-'||nmp[j]==' ')
                        temp=temp+'_'
                    else if(nmp[j]=='#'||nmp[j]=='.')
                        continue;
                    else
                        temp=temp+nmp[j];
                    
                }
                nmp=temp+'_'+woeid.toString();
                //alert(nmp)
                $scope.pname=nmp;
                break;
            }

        var url="https://telepathy.pythonanywhere.com/place/"+$scope.pname.toString();
        //console.log(url);
        $scope.purl="https://telepathy.pythonanywhere.com/"+$scope.pname.toString();
        var xmlhttp = new XMLHttpRequest();
        //var url = "myTutorials.txt";
        //console.log($scope.purl);

        xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $scope.allplace = eval(this.responseText);
            //alert(JSON.stringify(this.responseText));
            
         }
        };
        xmlhttp.open("GET", url, false);
        xmlhttp.send();
        var adddiv = document.getElementById("barchart");

        adddiv.innerHTML = '';
        var iframe = document.createElement('iframe');  
        iframe.height="800";
        iframe.width="1500";
        iframe.frameborder="0";
        iframe.src = $scope.purl;
        adddiv.appendChild(iframe);



    };


    $scope.pplay=function(con) {
       // alert("hhgxg");
        
       
        if(con=="Worldwide"){
              console.log(con);  
            // var id=data.id;
        $scope.pname="Worldwide_1";

        var url="https://telepathy.pythonanywhere.com/place/"+$scope.pname.toString();
        //console.log(url);
        $scope.purl="https://telepathy.pythonanywhere.com/"+$scope.pname.toString();
        var xmlhttp = new XMLHttpRequest();
        //var url = "myTutorials.txt";
        //console.log($scope.purl);

        xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            $scope.allplace = eval(this.responseText);
            //alert(JSON.stringify(this.responseText));
            
         }
        };
        xmlhttp.open("GET", url, false);
        xmlhttp.send();
        var adddiv = document.getElementById("barchart");

        adddiv.innerHTML = '';
        var iframe = document.createElement('iframe');  
        iframe.height="800";
        iframe.width="1500";
        iframe.frameborder="0";
        iframe.src = $scope.purl;
        //frameDoc = frame.contentDocument || frame.contentWindow.document;
        iframe.setStyles({ 'overflow': 'auto' });
        adddiv.appendChild(iframe);



        }

    };












    });