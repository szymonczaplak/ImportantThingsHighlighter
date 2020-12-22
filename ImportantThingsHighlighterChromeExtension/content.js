//alert("Hello from your Chrome extension!")
//

window.doSearch =  function(text,color="yellow") {
    var bodyText = document.body.innerHTML
    if (color!="transparent") {
      doSearch(bodyText,"transparent");
      }
    if (window.find && window.getSelection) {
        document.designMode = "on";
        var sel = window.getSelection();
        sel.collapse(document.body, 0);

        while (window.find(text)) {
            document.execCommand("HiliteColor", false, color);
            sel.collapseToEnd();
        }
        document.designMode = "off";
    } else if (document.body.createTextRange) {
        var textRange = document.body.createTextRange();
        while (textRange.findText(text)) {
            textRange.execCommand("BackColor", false, color);
            textRange.collapse(false);
        }
    }
}
var bodyText = document.body.innerHTML

chrome.runtime.sendMessage({thing: "url"}, function(response) {
//    alert(response.url);
    if(response.url.indexOf("medium.com") != -1 || response.url.indexOf("towardsdatascience.com") != -1){
       fetch('http://127.0.0.1:8000/', {
          method: 'POST',
          body: JSON.stringify({
            html: bodyText
          }),
          headers: {
            'Content-type': 'application/json; charset=UTF-8'
          }
        })
        .then(function(response) {
                if (response.status !== 200) {
                    alert('Looks like there was a problem. Status Code: ' +
                      response.status);
                    return;
              }
              // Examine the text in the response
              response.json().then(function(data) {

                data.important_things.forEach(function (item, index) {
                      window.doSearch(item);
                    });

//                alert("DONE")
              });
            }
        )

    }
    return true;
});
//
//var bodyText = document.body.innerHTML
//chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
//    let url = tabs[0].url;
//    if(tab.url.indexOf("medium.com") != -1){
//       fetch('http://127.0.0.1:8000/', {
//          method: 'POST',
//          body: JSON.stringify({
//            html: bodyText
//          }),
//          headers: {
//            'Content-type': 'application/json; charset=UTF-8'
//          }
//        })
//        .then(function(response) {
//                if (response.status !== 200) {
//                    alert('Looks like there was a problem. Status Code: ' +
//                      response.status);
//                    return;
//              }
//              // Examine the text in the response
//              response.json().then(function(data) {
//
//                data.important_things.forEach(function (item, index) {
//                      window.doSearch(item);
//                    });
//
//                alert("DONE")
//              });
//            }
//        )
//
//    }
//});
//find("member", false, true);


//var theText = document.getElementsByTagName("BODY")[0];
//var params = JSON.parse({'page': theText});
//
//function callback() {
//    if (xhr.readyState === XMLHttpRequest.DONE) {
//        if (xhr.status === 200) {
//            result = xhr.responseText;
//            jsoned = JSON.parse(result)
//            document.write(jsoned.html)
//        }
//        else{
//            alert("FAIL")
//            alert(xhr.status)
//        }
//    }
//};
//
//var xhr = new XMLHttpRequest();
//xhr.open("POST", "http://127.0.0.1:8000/hello", true);
//xhr.onreadystatechange = callback;
//xhr.send(params);

//var http = new XMLHttpRequest();
//var url = 'http://127.0.0.1:8000/hello';
//var params = JSON.parse({'page': theText});
//http.open('POST', url, true);
//
////Send the proper header information along with the request
//http.setRequestHeader('Content-type', 'application/json');
//
//http.onreadystatechange = function() {//Call a function when the state changes.
//    if(http.readyState == 4 && http.status == 200) {
//        alert(http.responseText);
//    }
//    alert('FAIL ' + http.status)
//}
//http.send(params);
