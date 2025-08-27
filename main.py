import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'Список покупок'
    product_list = ft.Column()

    filter_type = "all"

    def load_product():
        product_list.controls.clear()
        for product_id, product_text, bought in main_db.shopping_list(filter_type):
            product_list.controls.append(add_product_row(product_id, product_text, bought))
        page.update()

    def add_product_row(product_id, product_text, bought):
        product_field = ft.TextField(value=product_text, expand=True, read_only=True)

        product_checkbox = ft.Checkbox(
            value=bool(bought),
            on_change=lambda e: toggle_product(product_id, e.control.value)
        )

        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE,
            tooltip='Удалить',
            on_click=lambda e, id=product_id: delete_product(id)
        )

        return ft.Row([
            product_checkbox,
            product_field,
            delete_button  
        ])

    def add_product(_):
        if product_input.value:
            product_id = main_db.new_product(product_input.value)
            product_list.controls.append(add_product_row(product_id, product_input.value, None))
            product_input.value = ''
            page.update()

    def toggle_product(product_id, is_bought):
        main_db.update_product(product_id, bought=int(is_bought))
        load_product()

    def delete_product(product_id):
        main_db.delete_product(product_id)
        load_product()

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_product()

    product_input = ft.TextField(label='Введите новый продукт', expand=True)
    add_button = ft.ElevatedButton('Добавить', on_click=add_product)

    filter_buttons = ft.Row(controls=[
        ft.ElevatedButton("Все", on_click=lambda e: set_filter('all')),
        ft.ElevatedButton("Купленные", on_click=lambda e: set_filter('bought')),
        ft.ElevatedButton("Не купленные", on_click=lambda e: set_filter('not bought'))
        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(ft.Column([
        ft.Row([product_input, add_button]),
        filter_buttons,
        product_list
    ]))

    load_product()


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main, view=ft.WEB_BROWSER)
