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
touches it, or when run manually from the Actions tab.

## Previewing

Any static file server works. GitHub Pages serves the site under `/LastOneIPromiseSupport/`, so
serve the `website/` folder at that path to check links and the 404 page as they behave in
production.
