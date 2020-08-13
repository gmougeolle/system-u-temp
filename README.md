# 🎉 U — Les nouveaux Composants

**TODO : Write a proper description**

## 🚀 Getting started

We use `npm` here, it just works™

1. Setup Node on your platform however you want
2. Install dependencies using `npm install`
3. Run the development server using `npm start`
4. Visit `http://localhost:8000/` and get to work.

## 🥋 Be a good citizen

**Code Formatting & Linting**

We've already done our bikeshedding, you just need to setup your editor to get to coding quickly.

1. Setup [Editorconfig](https://editorconfig.org/) so that we don't have to fight over spaces and tabs.
2. We use both [Prettier](https://prettier.io/) in conjunction with [ESlint](https://eslint.org/) for both JS code formatting and linting, you'll just need to setup your editor to work with ESLint as Prettier is included through `eslint-plugin-prettier`.

**Branches & Commits**

Use the `dev` branch as your main source of truth, if you're not going for a hotfix create a `feature/<name>` branch and do your stuff in there, once everything looks good, rebase *YOUR* branch against the current version of `dev` and then merge it into `dev`, it may be a good thing to squash your commits beforhand if you don't want to clutter our log.

Currently we're using `master` and `release` as reserved branches for deployment, although using tags might be a better way to be sure of what's in production.

We use [Commitizen](https://github.com/commitizen/cz-cli) for our commits with `cz-emoji` mostly because it looks cool and provides a nice interactive CLI for writing commits. Just install the command line utility with `npm install -g commitizen` and then use `git cz` when comitting. It's always a good idea to provide a scope for your work, whether it's on a feature or some housekeeping on the repo. Referencing a ticket is extra cool, although there may or may not be a ticket for whatever you're commiting.

## 🏗 What do we use

**TODO : Do something**
