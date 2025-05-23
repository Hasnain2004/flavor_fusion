from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import User, Recipe, Ingredient, Contact
from .forms import UserRegisterForm, UserLoginForm, RecipeForm, IngredientForm, ContactForm

def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'recipes/welcome.html')

@login_required
def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/home.html', {'recipes': recipes})

@login_required
def about(request):
    return render(request, 'recipes/about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'  # Ensure all new registrations are regular users
            user.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'recipes/register.html', {'form': form})

def login_view(request):
    # Redirect authenticated users to home page
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'recipes/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

@login_required
def recipe_create(request):
    IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=3)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Recipe created successfully!')
                return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
        formset = IngredientFormSet()
    
    return render(request, 'recipes/recipe_form.html', {'form': form, 'formset': formset})

@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    IngredientFormSet = inlineformset_factory(
        Recipe, Ingredient, 
        form=IngredientForm, 
        extra=1,
        can_delete=True
    )
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        formset = IngredientFormSet(request.POST, instance=recipe)
        
        # Debug information
        print(f"POST request received: {request.POST}")
        print(f"Form is valid: {form.is_valid()}")
        if not form.is_valid():
            print(f"Form errors: {form.errors}")
            
        print(f"Formset is valid: {formset.is_valid()}")
        if not formset.is_valid():
            print(f"Formset errors: {formset.errors}")
            print(f"Formset non-form errors: {formset.non_form_errors()}")
            
            # Try to identify the specific issue
            for i, ingredient_form in enumerate(formset):
                if ingredient_form.errors:
                    print(f"Ingredient {i} errors: {ingredient_form.errors}")
                    print(f"Ingredient {i} data: {ingredient_form.data}")
                    print(f"Ingredient {i} instance: {ingredient_form.instance.pk if ingredient_form.instance else 'None'}")
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Recipe updated successfully!')
            return redirect('recipe_detail', pk=recipe.pk)
        else:
            # Add form errors to messages for visibility
            if form.errors:
                messages.error(request, f"Form errors: {form.errors}")
            if formset.errors:
                messages.error(request, f"Formset errors: {formset.errors}")
    else:
        form = RecipeForm(instance=recipe)
        formset = IngredientFormSet(instance=recipe)
    
    return render(request, 'recipes/recipe_form.html', {'form': form, 'formset': formset, 'recipe': recipe})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('recipe_list')
    
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'recipes/contact.html', {'form': form})
