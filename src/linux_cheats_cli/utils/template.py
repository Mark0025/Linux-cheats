import os
from string import Template
from loguru import logger

def load_template(template_name):
    """Load template from the templates directory"""
    template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'public', 'templates')
    template_path = os.path.join(template_dir, template_name)
    
    logger.debug(f"Attempting to load template from: {template_path}")
    try:
        with open(template_path, 'r') as f:
            content = f.read()
            # Convert string to Template object
            template = Template(content)
            logger.info(f"Successfully loaded template: {template_name}")
            return template
    except FileNotFoundError:
        logger.error(f"Template not found: {template_path}")
        raise

def render_template(template_name, context):
    """Render an HTML template with context"""
    try:
        logger.debug(f"Rendering template {template_name} with context: {context}")
        
        # If template extends another, load base template
        if 'extends' in context:
            logger.info(f"Template {template_name} extends {context['extends']}")
            base_template = load_template(context['extends'])
            # Process the base template with context
            result = base_template.safe_substitute(context)
            logger.debug("Base template rendered successfully")
            return result
        
        # Otherwise load and process the template directly
        template = load_template(template_name)
        result = template.safe_substitute(context)
        logger.debug("Template rendered successfully")
        return result
        
    except Exception as e:
        logger.exception(f"Failed to render template {template_name}")
        raise 