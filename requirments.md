Create a Django-based blog application with the following features and structure:

Category System

Each blog post must belong to one category.

Category fields: name, slug, description, created_at, is_active and feature_image.

Slug should be auto-generated from the name with editable.

Show category-wise post filtering.

Tags System

A blog post can have multiple tags (Many-to-Many relationship).

Tag fields: name, slug,is_active.

Slug should be auto-generated.

Allow searching posts by tag.

Blog/Post Module

Fields: title, slug, content, featuredimage, category (ForeignKey), tags (ManyToMany), author, status (draft/published), created_at, updated_at, published_at, is_active.

Slug auto-generated from title.

Only published posts should appear in the public view.

Admin Features

Register Category, Tag, and Post models in Django admin.

Enable search by title.

Add filters for category, tags, and status.

Auto-fill slug fields.

Frontend Requirements

Home page showing latest published posts.

Category page showing posts under a specific category.

Tag page showing posts under a specific tag.

Single blog details page.

Sidebar with category list and popular tags.

Extra Features (Optional but preferred)

Pagination on post listing.

SEO-friendly URLs using slugs.

Related posts section based on tags.

User have multiple role like admin editor etc.

Django>=5.2,<5.3
Pillow>=10.3.0
database postgresql, pgvector admin user hocche diu and pasword hocche diu@123456

frontend django template with tailwindcss