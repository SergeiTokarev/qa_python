# qa_python
# Описание тестов:
# 1. test_add_book
# Проверка добавления книг
# 2. test_add_book_twice
# Нельзя добавить одну и ту же книгу дважды
# 3. test_add_rating_to_absent_book_fails
# Нельзя выставить рейтинг книге, которой нет в списке
# 4. test_cant_set_rating_less_than_one
# Нельзя выставить рейтинг меньше 1
# 5. test_cant_set_rating_greater_than_ten
# Нельзя выставить рейтинг больше 10
# 6. test_absent_book_has_no_rating
# У не добавленной книги нет рейтинга
# 7. test_add_to_favorites
# Добавление книги в избранное
# 8. test_add_to_favorites_fails_if_not_in_ratings
# Нельзя добавить книгу в избранное, если её нет в словаре books_rating
# 9. test_delete_from_favorites
# Проверка удаления книги из избранного
# 10. test_get_list_of_favorites_books
# Получение списка избранных книг
# 11. test_get_books_rating
# Вывод рейтинга книги по ее имени
# 12. test_set_book_rating
# Добавление рейтинга книге
# 13. test_get_books_with_specific_rating
# Получение книги с указанным рейтингом
# 14. test_get_books_with_specific_rating_fails_if_no_books
#  Получение книги с указанным рейтингом если нет книги
# 15. test_get_books_with_specific_rating_fails_if_no_books_with_same
#  Получение книги с укаанным рейтингом если нет книги с таким рейтингом
# 16. test_get_books_with_specific_rating_fails_if_wrong_rating
# Добавление книги с рейтингом меньше 1
