from  common import press_any_key
from template_generator import *
from settings import *

if __name__ == '__main__':
    log = object
    try:
        settings = Settings()
        templateGenerator = TemplateGenerator(settings)
        templateGenerator.run()
    except Exception as inst:
        print type(inst)
        print(inst)
    else:
        print('TemplateGenerator successful done!')
    finally:
        print('Finish!')
        press_any_key()
