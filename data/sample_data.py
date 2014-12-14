single_submission_options = {
        'Username' : ('QA-User1', 'QA-User2', 'QA-User3'),
        'Password' : ('CapsAndN1umbers', '240823', 'lowercase'),
        'Email' : ('TestEmail@gmail.com', 'AReallyLongEmailLikeThis@gmail.com', '1234@4321.com'),
        'Phone Number' : ('2125555555', '7147777777'),
        'Account Type' : ('User', 'QA', 'Admin'),
        }

smoke_test = {
        'Username' : ('ImportantUser'), 
        'Password' : ('Sm0keTest1'),
        'Email' : ('CurrentTestUser@mywebsite.com'),
        'Phone Number' : ('7155555555'),
        'Account Type' : ('User'),
        }

form_fields = [
        ('Username', {
            'element_id': 'div_id_username',
            'input_function': '_type_into_text_field',
            'default_value': None,
        }),
        ('Password', {
            'element_id': 'div_id_password',
            'input_function': '_type_into_text_field',
            'default_value': None,
            }),
        ('Email', {
            'element_id': 'div_id_email',
            'input_function': '_type_into_text_field',
            'default_value': None,
            }),
        ('Phone Number', {
            'element_id': 'div_id_phone_number',
            'input_function': '_type_into_text_field',
            'default_value': None,
            }),
        ('Account Type', {
            'element_id': 'div_id_account_type',
            'input_function': '_select_from_dropdown',
            'default_value': None,
            }),
    ]
