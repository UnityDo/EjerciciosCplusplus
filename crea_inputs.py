import unreal

# Obtener el sistema de administración de assets
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Definir la ruta de la nueva carpeta
input_folder_path = "/Game/Input"

# Crear la nueva carpeta si no existe
if not unreal.EditorAssetLibrary.does_directory_exist(input_folder_path):
    unreal.EditorAssetLibrary.make_directory(input_folder_path)
    print(f"Carpeta creada en la ruta: {input_folder_path}")
else:
    print(f"La carpeta ya existe en la ruta: {input_folder_path}")

# Función para crear un nuevo asset
def create_asset(asset_class, asset_name, asset_path):
    factory = asset_tools.create_asset(asset_name, asset_path, asset_class, None)
    return factory


# Crear el Input Mapping Context (IMC_Snake)
imc_snake = create_asset(unreal.InputMappingContext, "IMC_Snake", input_folder_path)
print("IMC_Snake creado")

# Crear las Input Actions (IA_MoveUp, IA_MoveDown, IA_MoveLeft, IA_MoveRight)
ia_move_up = create_asset(unreal.InputAction, "IA_MoveUp", input_folder_path)
ia_move_down = create_asset(unreal.InputAction, "IA_MoveDown", input_folder_path)
ia_move_left = create_asset(unreal.InputAction, "IA_MoveLeft", input_folder_path)
ia_move_right = create_asset(unreal.InputAction, "IA_MoveRight", input_folder_path)
print("Input Actions creadas")

# Cargar los assets creados para modificarlos
imc_snake = unreal.EditorAssetLibrary.load_asset(f"{input_folder_path}/IMC_Snake")

# Crear una instancia de cada Input Action y asignarlas a una variable
ia_move_up = unreal.EditorAssetLibrary.load_asset(f"{input_folder_path}/IA_MoveUp")
ia_move_down = unreal.EditorAssetLibrary.load_asset(f"{input_folder_path}/IA_MoveDown")
ia_move_left = unreal.EditorAssetLibrary.load_asset(f"{input_folder_path}/IA_MoveLeft")
ia_move_right = unreal.EditorAssetLibrary.load_asset(f"{input_folder_path}/IA_MoveRight")

# Crear instancias de unreal.Key para cada tecla
key_w = unreal.Key()
key_s = unreal.Key()
key_a = unreal.Key()
key_d = unreal.Key()

key_w.set_editor_property("key_name","W")
key_s.set_editor_property("key_name","S")
key_a.set_editor_property("key_name","A")
key_d.set_editor_property("key_name","D")

# Mapear las acciones a las teclas usando instancias de unreal.Key
imc_snake.map_key(ia_move_up, key_w)
imc_snake.map_key(ia_move_down, key_s)
imc_snake.map_key(ia_move_left, key_a)
imc_snake.map_key(ia_move_right, key_d)

# Guardar los cambios en el contexto de mapeo de entrada
unreal.EditorAssetLibrary.save_loaded_asset(imc_snake)
