from pyngrok import ngrok
ngrok.set_auth_token("2Kk2u5qxrYjSrDi10R4E8StBZ6E_3qwzmJgVy7zTkcpTeaqjK")
tunnel = ngrok.connect(5005)
