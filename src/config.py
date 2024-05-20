URL_FOR_GET_PROFESSIONAL_ROLES = "https://api.hh.ru/professional_roles"

START_URL = "https://vladivostok.hh.ru/search/vacancy?L_save_area=true&text=&excluded_text=&professional_role="
END_URL = "&area=22&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&hhtmFrom=vacancy_search_filter"

START_URL_FOR_PAGES = "https://vladivostok.hh.ru/search/vacancy?L_save_area=true&area=22&items_on_page=20&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&professional_role="
END_URL_FOR_PAGES = "&text=&page="

SPECIALIZATIONS_FILE_PATH = "src/data/spec.txt"

INFO_TEXT = """Начните вводить название интересующей вас профессии, 
            нажмите Enter и перед вами появится список похожих профессий, 
            введите id профессии и ожидайте выполнение запроса
            Либо же вы можете ввести id професси сразу
            Введите 'q' для выхода"""

LIMIT_SPECIALIZATION_OUTPUT = 7
