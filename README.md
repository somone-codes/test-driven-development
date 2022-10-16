# This is project for TDD for python


## Handy Commands:
- ### Testing:
  - #### Unit Testing:
    - ##### Lists Application:
       - #### Forms Module:
         - *python manage.py test lists.tests.test_forms*
       - #### Views Module:
         - *python manage.py test lists.tests.test_views*
         - *python manage.py test lists.tests.test_views.ListViewTest*
       - #### Models Module:
         - *python manage.py test lists.tests.test_models*
         - *python manage.py test lists.tests.test_models.ItemModelTest*
  - #### Functional Testing:
    - *python manage.py test functional_tests*
    - *python manage.py test functional_tests.test_list_item_validation*
    - *python manage.py test functional_tests.test_list_item_validation.ItemValidationTest*
    - *python manage.py test functional_tests.test_list_item_validation.ItemValidationTest.test_cannot_add_duplicate_items*
- ### Migrations:
   - *python manage.py makemigrations*
   - *python manage.py migrate [--noinput]*