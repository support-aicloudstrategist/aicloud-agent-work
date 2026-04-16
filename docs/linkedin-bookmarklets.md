# LinkedIn Bookmarklets for AICloudStrategist Outreach

Two bookmarklets that cut 30 seconds off every connection request and every Day-2 DM. Used across Anushka's 30-day plan of ~500 connection requests + ~200 Day-2 follow-ups, they save **4–6 hours of total clicking**.

---

## What a bookmarklet is

A bookmark that contains JavaScript instead of a URL. When clicked, it runs the JS on whatever LinkedIn page is currently open. No extension, no install, no server. Runs inside Anushka's own logged-in browser, so LinkedIn sees it as her click.

**Honest limitation:** LinkedIn's HTML structure changes every 2–4 weeks. If a bookmarklet suddenly stops working, it means LinkedIn updated their UI — ping Raj and I'll update the selectors.

---

## Install (one-time, 30 seconds)

### In Chrome / Edge / Brave:

1. Right-click the bookmarks bar → "Add page..."
2. Name: `LI-Connect-Anushka`
3. URL: paste the full JS snippet from **Bookmarklet 1** below (including the `javascript:` prefix)
4. Save
5. Repeat for **Bookmarklet 2** (name it `LI-DM-Anushka`)

If you don't see the bookmarks bar, press `Ctrl+Shift+B`.

### In Safari:

1. Bookmarks → Add Bookmark → save any random URL with the desired name
2. Bookmarks → Edit Bookmarks → find the one you just saved → paste the JS into the Address field, replacing the URL
3. Save

---

## Bookmarklet 1 — "LI-Connect-Anushka"

**What it does:** You're on a LinkedIn profile page (e.g. `linkedin.com/in/someone-cto`). Click the bookmarklet. It:

1. Auto-clicks the "Connect" button on the profile
2. Auto-clicks "Add a note" in the dialog
3. Pastes the Anushka connection-request template, auto-filling `{{FirstName}}` from the profile's visible name and `{{Company}}` from the experience section where possible
4. **Leaves the cursor in the note field** so Anushka can personalise the first sentence before hitting Send

She reviews, tweaks, clicks Send. ~5 seconds per request vs ~30 seconds without.

**The code (paste verbatim as the bookmark URL):**

```javascript
javascript:(function(){
  var firstName = (document.querySelector('h1')?.innerText?.trim().split(/\s+/)[0]) || '[Name]';
  var company = '';
  try {
    var exp = document.querySelector('section[data-view-name="profile-component-entity"]');
    var m = exp?.innerText?.match(/([A-Z][a-zA-Z0-9&.,\- ]{2,60})/);
    if (m) company = m[1].trim().split('\n')[0];
  } catch(e){}
  if (!company) company = '[Company]';
  var msg = 'Hi ' + firstName + ' — noticed you are leading engineering at ' + company + '. I run AICloudStrategist, a focused FinOps and cloud architecture practice for Indian tech companies. Would be good to connect — keen to hear what is on your plate in 2026. — Anushka';
  function findConnect(){
    var btns = Array.from(document.querySelectorAll('button'));
    return btns.find(function(b){
      var t = (b.innerText || b.textContent || '').trim();
      return t === 'Connect' || t === 'Invite to connect' || /^Connect$/i.test(t);
    }) || btns.find(function(b){ return /connect/i.test(b.getAttribute('aria-label') || ''); });
  }
  var connectBtn = findConnect();
  if (!connectBtn) {
    alert('Connect button not found. You may need to click "More" first, or this person is already a 1st-degree connection.');
    return;
  }
  connectBtn.click();
  setTimeout(function(){
    var addNote = Array.from(document.querySelectorAll('button')).find(function(b){
      return /add a (note|free note)/i.test(b.innerText || '');
    });
    if (!addNote) {
      alert('Add-a-note button not found. If LinkedIn skipped straight to the note field, just paste manually: \n\n' + msg);
      return;
    }
    addNote.click();
    setTimeout(function(){
      var ta = document.querySelector('textarea[name="message"], textarea#custom-message');
      if (!ta) {
        alert('Note textarea not found. Paste manually: \n\n' + msg);
        return;
      }
      var setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
      setter.call(ta, msg);
      ta.dispatchEvent(new Event('input', {bubbles: true}));
      ta.focus();
      ta.setSelectionRange(msg.indexOf(firstName), msg.indexOf(firstName) + firstName.length);
    }, 400);
  }, 400);
})();
```

### How to use

1. Open any 2nd or 3rd-degree LinkedIn profile (e.g. a CTO at a target company)
2. Click the `LI-Connect-Anushka` bookmarklet
3. Dialog opens, note pre-filled with name and company inferred from the profile
4. Review the first sentence — change or personalise if you want
5. Click **Send**

### Fallback

If the bookmarklet's auto-detection of Company is wrong (it shows `[Company]` or picks up a wrong string), edit it manually in the note before sending. The worst case is it pastes the template with bracket placeholders that you edit in 5 seconds.

---

## Bookmarklet 2 — "LI-DM-Anushka"

**What it does:** You're in a LinkedIn DM thread with someone who just accepted your connection request. Click the bookmarklet. It pastes the Day-2 template (thank-you + free AWS Checklist PDF link) into the message box, with the first name auto-filled.

**The code:**

```javascript
javascript:(function(){
  var firstName = '[Name]';
  try {
    var h = document.querySelector('.msg-entity-lockup__entity-title, .msg-thread__link-to-profile h2, h2');
    if (h) firstName = (h.innerText || h.textContent || '').trim().split(/\s+/)[0];
  } catch(e){}
  var msg = 'Thanks for connecting, ' + firstName + '.\n\nI put together an AWS Cost Optimisation Checklist — 30 leak points we see repeatedly in mid-size Indian cloud accounts. No form, just the PDF:\naicloudstrategist.com/aws-checklist.html\n\nIf your team is on AWS and the bill has been creeping up, it may flag a few quick wins. Happy to talk through any of it.\n\n— Anushka';
  var editor = document.querySelector('.msg-form__contenteditable[contenteditable="true"], div[role="textbox"][contenteditable="true"]');
  if (!editor) {
    alert('Message editor not found. Open the DM thread, click in the message box, then click the bookmarklet again. Or paste manually: \n\n' + msg);
    return;
  }
  editor.focus();
  editor.innerText = msg;
  editor.dispatchEvent(new Event('input', {bubbles: true}));
  editor.dispatchEvent(new Event('change', {bubbles: true}));
})();
```

### How to use

1. Someone accepts your connection request (notification on LinkedIn)
2. Click their name to open a DM thread
3. Click the `LI-DM-Anushka` bookmarklet
4. Message appears with their first name pre-filled
5. Review, click **Send**

---

## Tips

- **Clear your own clipboard** before LinkedIn sessions — a misfired paste can leak sensitive text
- **Don't run both bookmarklets on the same page** — they target different UI elements, and running the wrong one on the wrong page triggers an alert
- **If an alert says "button not found,"** it usually means LinkedIn updated their UI. Paste manually from the fallback alert message, then ping Raj to update the bookmarklet
- **Never exceed 15 connection requests per day** regardless of tool speed — LinkedIn throttles based on request count, not how fast you click
- **The connection-request bookmarklet only runs on the profile itself.** It won't work on search result pages — you must click into the profile first

---

## Why these two specifically

These are the two highest-frequency, lowest-variance actions in the 30-day connection plan:

- Connection requests: ~500 over 30 days (segments 1–6 in `docs/linkedin-connection-request-plan.md`)
- Day-2 acceptance messages: ~200 (assuming 40% accept rate)

Combined time saved: ~5 hours in the first month alone. Worth the 30-second install.

---

## Future bookmarklets (not built yet, on request)

- **Profile → CRM copy** — one click copies name, role, company, URL formatted for Notion
- **Comment drafter** — one click generates an Anushka-voice thoughtful comment on a target CTO's post
- **Quick-follow** — follows a user + clicks Connect if not already connected
- **Hashtag scanner** — on any LinkedIn hashtag feed, extracts top 20 recent post authors for targeting

Tell Raj which ones would help next.

---

*AICloudStrategist · Anushka B · Founder-led. Enterprise-reviewed.*
