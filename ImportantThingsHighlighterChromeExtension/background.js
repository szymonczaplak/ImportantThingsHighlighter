chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.thing == "url"){
        chrome.tabs.query({
          active: true,
          currentWindow: true
        }, function(tabs) {
          var tab = tabs[0];
          var url = tab.url;
          sendResponse({"url": url})
          console.log("URL sent" + url)
          return true;
        });
    }
    return true;
  });
