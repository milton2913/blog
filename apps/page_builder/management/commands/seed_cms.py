import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from menus.models import Menu, MenuItem
from page_builder.models import Page, PageBlock
from blog.models.post import Post
from blog.models.category import Category
from django.contrib.contenttypes.models import ContentType

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with dynamic menus and pages'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding CMS data...")

        # 1. Create Menus
        header_menu, _ = Menu.objects.get_or_create(name="Main Menu", slug="main-menu")
        footer_menu, _ = Menu.objects.get_or_create(name="Footer Menu", slug="footer-menu")

        # Clear existing items for re-seeding if necessary (optional)
        MenuItem.objects.filter(menu__in=[header_menu, footer_menu]).delete()

        # 2. Get some content to link to
        posts = list(Post.objects.all())
        categories = list(Category.objects.all())
        
        post_ct = ContentType.objects.get_for_model(Post)
        category_ct = ContentType.objects.get_for_model(Category)

        # 3. Seed Header Menu (5 items)
        self.stdout.write("Seeding Header Menu...")
        
        MenuItem.objects.create(menu=header_menu, title="Home", link_type='manual', url="/", order=1)
        
        for i, cat in enumerate(categories[:2]): # Order 2, 3
            MenuItem.objects.create(
                menu=header_menu, 
                title=cat.name, 
                link_type='object', 
                content_type=category_ct, 
                object_id=cat.id, 
                order=i+2
            )
            
        MenuItem.objects.create(menu=header_menu, title="Services", link_type='manual', url="/pages/services/", order=4)
        MenuItem.objects.create(menu=header_menu, title="Google", link_type='manual', url="https://google.com", order=5)
        
        # 4. Seed Footer Menu (5 items)
        self.stdout.write("Seeding Footer Menu...")
        MenuItem.objects.create(menu=footer_menu, title="About", link_type='manual', url="/pages/about/", order=1)
        MenuItem.objects.create(menu=footer_menu, title="Privacy Policy", link_type='manual', url="/pages/privacy-policy/", order=2)
        MenuItem.objects.create(menu=footer_menu, title="Terms of Service", link_type='manual', url="/pages/terms-conditions/", order=3)
        MenuItem.objects.create(menu=footer_menu, title="Contact", link_type='manual', url="/pages/contact/", order=4)
        MenuItem.objects.create(menu=footer_menu, title="Blog Archive", link_type='manual', url="/", order=5)
        
        # 5. Seed Dynamic Pages (10 pages)
        self.stdout.write("Seeding 10 Dynamic Pages...")
        Page.objects.filter(slug__startswith='seed-').delete() # Cleanup seeded pages
        Page.objects.filter(slug='services').delete()
        
        # Create an explicit Services page
        services_page = Page.objects.create(
            title="Our Services",
            slug="services",
            status='published',
            meta_title="Professional Services - Django Blog",
            meta_description="Explore our range of professional web development and consulting services."
        )
        PageBlock.objects.create(
            page=services_page,
            block_type='hero',
            data={"headline": "Professional Services", "subheadline": "We build scalable solutions for modern businesses."},
            order=1
        )

        page_ct = ContentType.objects.get_for_model(Page)

        for i in range(10):
            title = fake.sentence(nb_words=3).replace(".", "")
            page = Page.objects.create(
                title=title,
                slug=f"seed-{slugify(title)}",
                status='published',
                meta_title=f"SEO {title}",
                meta_description=fake.paragraph()
            )
            
            # Add some blocks to each page
            # Hero
            PageBlock.objects.create(
                page=page,
                block_type='hero',
                data={
                    "headline": f"Welcome to {title}",
                    "subheadline": fake.sentence(),
                    "button_text": "Learn More",
                    "button_url": "#"
                },
                order=1
            )
            
            # Rich Text
            PageBlock.objects.create(
                page=page,
                block_type='text',
                data={
                    "text": fake.paragraphs(nb=3)
                },
                order=2
            )
            
            # CTA
            PageBlock.objects.create(
                page=page,
                block_type='cta',
                data={
                    "title": "Want to join us?",
                    "text": "Sign up for our newsletter today!",
                    "button_text": "Sign Up",
                    "button_url": "/accounts/register/"
                },
                order=3
            )
            
            # order=3

        self.stdout.write(self.style.SUCCESS("Successfully seeded CMS and Menus!"))
