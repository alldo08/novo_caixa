-- Special thanks to Gotlag for these recipe functions
local function replace_ingredient(ingredients, old_ingredient, new_ingredient)
    for i,ingredient in pairs(ingredients) do
        if ingredient.name then
            if ingredient.name == old_ingredient then
                ingredient.name = new_ingredient
            end
        elseif ingredient[1] == old_ingredient then
            ingredient[1] = new_ingredient
        end
    end
end


local function update_recipe(recipe, old_ingredient, new_ingredient)
    if data.raw.recipe[recipe].ingredients then
        replace_ingredient(data.raw.recipe[recipe].ingredients, old_ingredient, new_ingredient)
    end
    if data.raw.recipe[recipe].normal then
        replace_ingredient(data.raw.recipe[recipe].normal.ingredients, old_ingredient, new_ingredient)
    end
    if data.raw.recipe[recipe].expensive then
        replace_ingredient(data.raw.recipe[recipe].expensive.ingredients, old_ingredient, new_ingredient)
    end
end

update_recipe("concrete", "iron-ore", "iron-stick")

if mods["Dectorio"] then
    update_recipe("dect-concrete-grid", "iron-ore", "iron-stick")
end
