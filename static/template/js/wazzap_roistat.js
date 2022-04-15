(function () {
  function ChangeLinkWA() {

    // Токен {wz_metric} используется для подстановки кода аналитики.
    // Убедитесь, чтобы токен и текст, в котором он прописан,
    // были разделены как минимум одним символом пробела.

    this.text = 'У меня есть вопрос. Номер обращения: {wz_metric}';
    this.cookieSource = 'roistat_visit';
    this.observer = null;
  }

  ChangeLinkWA.prototype.editLink = function (url, id) {
    if (decodeURIComponent(url.split('text=')[1]) === this.text.replace(/{wz_metric}/gi, id)) return;
    
    var regexNumberPhone = /\d+/;
    if(!regexNumberPhone.test(url)) return
    var phone = url.match(regexNumberPhone)[0];
    var host = url.split(phone)[0];

    var newUrl = (host === 'https://wa.me/') 
      ? `${host}${phone}?text=${this.text.replace(/{wz_metric}/gi, id)}`
      : `${host}${phone}&text=${this.text.replace(/{wz_metric}/gi, id)}`
    
    return newUrl;
  };

  ChangeLinkWA.prototype.getCookie = function (name) {
    var cookie = document.cookie;
    var matches = cookie.match(new RegExp(`(?:^|; )${ name.replace(/([.$?*|{}()[]\/+^])/g, '\\$1') }=([^;]*)`));
    
    return matches ? decodeURIComponent(matches[1]) : undefined;
  };

  ChangeLinkWA.prototype.censusLinks = function () {
    var links = document.querySelectorAll('[href*="//wa.me"], [href*="//api.whatsapp.com/send"], [href*="//web.whatsapp.com/send"], [href^="whatsapp://send"]');
    var id = this.getCookie(this.cookieSource);
    var that = this;

    links.forEach(function(link) {
      var newLink = that.editLink(link.href, id)

      if (newLink) link.href = newLink;
    });
  };

  ChangeLinkWA.prototype.initObserver = function () {
    var that = this;
    this.observer = new MutationObserver(function () {
      that.censusLinks();
    });
  };

  ChangeLinkWA.prototype.startObserver = function () {
    this.observer.observe(document.body, {
      attributeFilter: ['href'],
      attributes: true,
      childList: true,
      attributeOldValue: true,
      characterDataOldValue: true,
      characterData: true,
      subtree: true,
    });
  };

  ChangeLinkWA.prototype.init = function () {
    this.initObserver();
    this.startObserver();
  };

  if (!(window.__wz_scripts && window.__wz_scripts.scriptsChangeLinkWA)) {
    if (!window.__wz_scripts) window.__wz_scripts = {};
    
    window.__wz_scripts.scriptsChangeLinkWA = new ChangeLinkWA();
    window.__wz_scripts.scriptsChangeLinkWA.init();
  }
})();