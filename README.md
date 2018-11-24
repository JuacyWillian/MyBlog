# My Blog

Sit doloribus aut alias minus quis. Rerum consequatur et ea non dicta cum ipsam. Omnis aliquam quos necessitatibus dolorum et esse. Temporibus nisi repellat iste praesentium illo et facere sed.

Et assumenda sit distinctio exercitationem sequi totam enim. Qui quia sequi quo. Esse eum dolorem neque quisquam quia. Enim consequuntur voluptatibus officiis beatae sunt. Beatae in et doloribus et esse est reiciendis natus. Optio omnis debitis consequatur.

#### funcionalidades

#### rotas
* / -> index
* /post/:post_id -> view post
* /tag/:tag_name -> filter posts by tag
* /category/:category_name -> filter posts by category
* /login -> login # default: username=admin, password=secret
* /logout -> logout
* /admin -> admin dashboard
* /admin/postview -> post crud

#### instalação

```python
git clone myblog
cd myblog
pip install -r requirements.txt
```

#### Variaveis de ambiente
##### Linux / MacOS
```
export FLASK_APP=app/app:create
export FLASK_MODE=development
export SECRET_KEY={{ secure secret key }}
```

##### Windows
```
set FLASK_APP=app/app:create
set FLASK_MODE=development
set SECRET_KEY={{ secure secret key }}
```

##### Usando arquivo .env
crie um arquivo .env no diretorio raiz e adicione as varieveis de ambiente nele da seguinte forma CHAVE=VALOR

exemplo: .env
```envfile
FLASK_APP=app/app:create
FLASK_MODE=development
SECRET_KEY={{ secure secret key }}
```

#### rodando
```
flask run
```

#### deploy
em breve
