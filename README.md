# Last One, I Promise — Support Website

Support, Privacy Policy, Terms of Use and data-deletion pages for the **Last One, I Promise** iPhone
app, published at <https://vladimiramiorkov.github.io/LastOneIPromiseSupport/>.

Questions or problems with the app? Email [lastoneipromise.app@proton.me](mailto:lastoneipromise.app@proton.me).

## Structure

Plain HTML and CSS, no build step. Everything published lives in `website/`:

| Page | File |
|---|---|
| Support + FAQ + contact | `website/index.html` |
| Privacy Policy | `website/privacy/index.html` |
| Terms of Use | `website/terms/index.html` |
| Delete your data | `website/delete-data/index.html` |

`website/styles.css` holds shared styling (light/dark), and `website/images/` holds the app icon.
`.github/workflows/pages.yml` deploys `website/` to GitHub Pages on every push to `main` that
touches it.

## Testing locally

```bash
./serve.sh
```

Opens <http://localhost:8000/LastOneIPromiseSupport/>, served the same way GitHub Pages serves it
(including the 404 page). Pass a port to use a different one, e.g. `./serve.sh 8080`. Ctrl+C stops it.
