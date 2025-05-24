from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Collect static files and restart server for development'

    def add_arguments(self, parser):
        parser.add_argument(
            '--no-restart',
            action='store_true',
            help='Only collect static files, do not restart server',
        )

    def handle(self, *args, **options):
        self.stdout.write('🔄 Collecting static files...')
        
        # Collect static files
        call_command('collectstatic', interactive=False, verbosity=0)
        
        self.stdout.write(
            self.style.SUCCESS('✅ Static files collected successfully!')
        )
        
        if not options['no_restart']:
            self.stdout.write('💡 Tip: Restart your development server to see changes when DEBUG=False')
            self.stdout.write('    Use --no-restart flag to skip this message')