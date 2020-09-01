# 🎉 U — Flask U

A tiny Flask app to simulate the real deal.

## 🚀 Getting started

1. Install the requirements (maybe create and activate a `venv` first):

`pip install -r requirements.txt`

2. Just start™

`python run.py`

3. Go to `http://localhost:5500/home`

4. There's no 4

**Caution : you need to build the UI-Kit first !**

## 🏗 What now ?

We're trying to mimic the structure of the final integration with `udata`, you can find most of the pages inside the `template` folder.
Whenever you find a structure that can be reused create a `templates/<component>` subfolder so that we can keep things DRY.

Some templates to look out for :

- `home.html` : well, duh.
- `header.html` and `footer.html` : same idea.
- `raw.html` : contains the general html structure exposing a `body` block where we can write our page's body.
- `base.html` : contains some extra html structure exposing a `content` block for our page's content.
- `subnav-large.html`, `publish-action-modal.html` and `carousel.html` : **TODO**

Here are our reusable components :

- `dataset` : datasets listings used in many pages.
- `reuse` : cards for displaying dataset reused in the real world.
- `participez` : is the large blue callout seen on multiple pages.
- `macros` : **TODO**
- `svg` : contains SVG assets to be included in our pages.
