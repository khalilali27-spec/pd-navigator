# PD Management Navigator

An installable, offline-capable web app (PWA): a clinical pathway for Parkinson disease
management covering diagnosis, starting treatment, the therapeutic window, adjusting therapy,
non-motor symptoms, advanced therapies and late-stage care. It is a learning tool for clinicians
and does not replace clinical judgment or product labeling.

## Install
- **iPhone / iPad (Safari):** open the site, tap Share, then **Add to Home Screen**.
- **Android (Chrome):** tap **Install** when prompted, or ⋮ → **Install app**.
- **Mac / Windows (Chrome or Edge):** click the install icon in the address bar.

After the first open, everything (fonts, the patient handout PDF and all pathway content) is
stored on the device and works with no signal. Checklist ticks, your place in each pathway and
LED calculator entries are saved on the device only. Nothing is sent anywhere.

## Updating
Edit the files, then run `python3 build.py` to regenerate `sw.js`. It stamps a content hash, so
installed copies show "An updated version is ready → Reload" the next time they open.
