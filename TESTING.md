[Home Page](testing/home-page.png)

# Testing Documentation for Fashion Tech

## Validation

### HTML Validation

All pages pass HTML Validation at [W3C markup validation service](https://validator.w3.org/)

#### HTML Validation Errors

- Initial errors in HTML that were fixed during validation.

![HTML Validation Error](testing/html-error.png)

![HTML Validation Error](testing/html-error-2.png)

![HTML Validation Error](testing/html-error-3.png)

| Page | Result | Screenshot |
| --- | --- | --- |
| Home | Pass | ![HTML validation](testing/html-home.png) |
| About | Pass | ![HTML validation](testing/html-about.png) |
| Sign Up | Pass | ![HTML validation](testing/html-sign-up.png) |
| Sign In | Pass | ![HTML validation](testing/html-sign-in-form.png) |
| Sign Out | Pass | ![HTML validation](testing/html-sign-out.png) |
| Article Detail | Pass | ![HTML validation](testing/html-article.png) |

### CSS Validation

CSS was validated using the [W3C CSS Validation Service]().

| File | Result | Screenshot |
| --- | --- | --- |
| style.css | Pass | ![CSS validation](testing/css-validation.png) |

**Notes** 
- No errors found

### Javascript Validation

Javascript was validated using [JSHint](https://jshint.com/).

| File | Result | Screenshot |
| --- | --- | --- |
| comments.js | Pass | ![JS validation](testing/js-validation.png) |

**Configuration:**
- `esversion: 6` configured for ES6 syntax
- `globals bootstrap` configured for Bootstrap modal

**Notes**
- No errors found
- No undefined variables

### Python Validation

Python code was validated using PEP8 standards, using [CI Python Linter](https://pep8ci.herokuapp.com/).

| File | Result | Screenshot |
| --- | --- | --- |
| blog/views.py | Pass | ![Python validation](testing/blog-views.png) |
| blog/models.py | Pass | ![Python validation](testing/blog-models.png) |
| blog/forms.py | Pass | ![Python validation](testing/blog-forms.png) |
| blog/urls.py | Pass | ![Python validation](testing/blog-urls.png) |
| blog/admin.py | Pass | ![Python validation](testing/blog-views.png) |
| blog/apps.py | Pass | ![Python validation](testing/blog-apps.png) |
| about/views.py | Pass | ![Python validation](testing/about-views.png) |
| about/models.py | Pass | ![Python validation](testing/about-models.png) |
| about/forms.py | Pass | ![Python validation](testing/about-forms.png) |
| about/urls.py | Pass | ![Python validation](testing/about-urls.png) |
| about/apps.py | Pass | ![Python validation](testing/about-apps.png) |
| fashiontech/urls.py | Pass | ![Python validation](testing/fashiontech-urls.png) |

**Notes**
- All Python files pass PEP8 validation
- No lines exceed 79 characters
- No trailing whitespace

## Manual Feature Testing



## User Stories Testing

### Visitor Goals

**View Articles**
- User Story: I can view articles to learn about fashion technology
- Feature: Home page displays paginated article list
- Test: Loaded home page, verified 6 articles display with pagination
- Result: ✅ Pass

**Read Full Articles**
- User Story: I can read full articles for detailed insights
- Feature: Article detail page shows complete content
- Test: Clicked article link, verified full content displays
- Result: ✅ Pass

**Create Account**
- User Story: I can create an account to comment on articles
- Feature: Sign Up form with username, email, password fields
- Test: Filled registration form, submitted, account created
- Result: ✅ Pass

**Submit Collaboration**
- User Story: I can contact site owner to propose collaboration
- Feature: Collaboration form on About page
- Test: Submitted form, verified in admin panel
- Result: ✅ Pass

### Registered User Goals

**View Articles**
- User Story: I can view articles to learn about fashion technology
- Feature: Home page displays paginated article list
- Test: Loaded home page, verified 6 articles display with pagination
- Result: ✅ Pass

**Read Full Articles**
- User Story: I can read full articles for detailed insights
- Feature: Article detail page shows complete content
- Test: Clicked article link, verified full content displays
- Result: ✅ Pass

**Create Account**
- User Story: I can create an account to comment on articles
- Feature: Sign Up form with username, email, password fields
- Test: Filled registration form, submitted, account created
- Result: ✅ Pass

**Submit Collaboration**
- User Story: I can contact site owner to propose collaboration
- Feature: Collaboration form on About page
- Test: Submitted form, verified in admin panel
- Result: ✅ Pass
