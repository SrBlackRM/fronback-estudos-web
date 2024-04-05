const AppError = require("../utils/AppError")

class UsersController {
    create(request, response){
        const { name, email, password, isAdmin } = request.body;

        if(!name){
            throw new AppError("Nome de usuário não informado!");
        }

        if(!isAdmin){
            throw new AppError("Usuário não permitido",302);
        }

        response.status(201).json({name, email})
    }
}

module.exports = UsersController;