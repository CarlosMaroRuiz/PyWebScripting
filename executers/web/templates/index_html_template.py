INDEX_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Automatizado</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <style>
        body {
            background: linear-gradient(90deg, #306998, #FFD43B, #4B8BBE);
            background-size: 300% 300%;
            animation: gradient-animation 8s ease infinite;
        }

        @keyframes gradient-animation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center px-4">
    <div class="bg-white shadow-2xl rounded-2xl p-8 sm:p-12 max-w-md sm:max-w-lg md:max-w-2xl text-center transform transition hover:scale-105">
        <h1 class="text-4xl sm:text-5xl font-extrabold text-blue-800 mb-6">
            🚀 Proyecto Automatizado
        </h1>
        <p class="text-gray-700 text-lg sm:text-xl leading-relaxed">
            <span class="text-yellow-500 font-semibold">pyWeb</span> es un script automatizado para la generación de plantillas de carpetas
            y estructuras de proyectos web utilizando arquitectura en capas. Diseñado para automatizar el entorno de trabajo en el desarrollo de aplicaciones
            <span class="font-semibold text-blue-800">Fullstack</span>, así como la creación de APIs REST sencillas con
            <span class="font-semibold text-blue-600">FastAPI</span> y <span class="font-semibold text-blue-600">Flask</span>.
        </p>
    </div>
</body>
</html>
"""
