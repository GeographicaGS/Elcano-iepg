# coding=UTF8

"""
Constants
"""
lang = ["en", "es"]

years = [1990, 1995, 2000, 2005, 2010, 2011, 2012, 2013]

families = ["iepg", "iepe", "context"]

blocks = {
    "XBEU": {
        "key": "european_union",
        "name_en": "European Union",
        "name_es": "Unión Europea",
        "members": {
            "1990": ["ES", "FR", "IE"],
            "1995": ["ES", "FR", "IE"],
            "2000": ["ES", "FR", "IE"],
            "2005": ["ES", "FR", "IE"],
            "2010": ["ES", "FR", "IE"],
            "2011": ["ES", "FR", "IE"],
            "2012": ["ES", "FR", "IE"],
            "2013": ["ES", "FR", "IE"]
        }
    },
    "XBE2": {
        "key": "europe",
        "name_en": "Europe",
        "name_es": "Europa",
        "members": {
            "1990": ["ES", "FR", "IE"],
            "1995": ["ES", "FR", "IE"],
            "2000": ["ES", "FR", "IE"],
            "2005": ["ES", "FR", "IE"],
            "2010": ["ES", "FR", "IE"],
            "2011": ["ES", "FR", "IE"],
            "2012": ["ES", "FR", "IE"],
            "2013": ["ES", "FR", "IE"]
        }
    },
    "XBLA": {
        "key": "latin_america",
        "name_en": "Latin America",
        "name_es": "América Latina",
        "members": {
            "1990": ["ES", "FR", "IE"],
            "1995": ["ES", "FR", "IE"],
            "2000": ["ES", "FR", "IE"],
            "2005": ["ES", "FR", "IE"],
            "2010": ["ES", "FR", "IE"],
            "2011": ["ES", "FR", "IE"],
            "2012": ["ES", "FR", "IE"],
            "2013": ["ES", "FR", "IE"]
        }
    },
    "XBNA": {
        "key": "north_america",
        "name_en": "North America",
        "name_es": "América del Norte",
        "members": {
            "1990": ["ES", "FR", "IE"],
            "1995": ["ES", "FR", "IE"],
            "2000": ["ES", "FR", "IE"],
            "2005": ["ES", "FR", "IE"],
            "2010": ["ES", "FR", "IE"],
            "2011": ["ES", "FR", "IE"],
            "2012": ["ES", "FR", "IE"],
            "2013": ["ES", "FR", "IE"]
        }
    },
    "XBAP": {
        "key": "asia_and_pacific",
        "name_en": "Asia & Pacific",
        "name_es": "Ásia y Pacífico",
        "members": {
            "1990": ["ES", "FR", "IE"],
            "1995": ["ES", "FR", "IE"],
            "2000": ["ES", "FR", "IE"],
            "2005": ["ES", "FR", "IE"],
            "2010": ["ES", "FR", "IE"],
            "2011": ["ES", "FR", "IE"],
            "2012": ["ES", "FR", "IE"],
            "2013": ["ES", "FR", "IE"]
        }
    },
    "XBME": {
        "key": "magreb_middle_east",
        "name_en": "Magreb & Middle East",
        "name_es": "Magreb y Oriente Medio",
        "members": {
            "1990": ["ES", "FR", "IE"],
            "1995": ["ES", "FR", "IE"],
            "2000": ["ES", "FR", "IE"],
            "2005": ["ES", "FR", "IE"],
            "2010": ["ES", "FR", "IE"],
            "2011": ["ES", "FR", "IE"],
            "2012": ["ES", "FR", "IE"],
            "2013": ["ES", "FR", "IE"]
        }
    }
}

variables = {
    "iepg_energy": {
        "key": "energy",
        "family": "iepg",
        "name_en": "Energy",
        "name_es": "Energía",
        "table": "iepg_data.iepg_final_data",
        "column": "energy"},
    "iepg_primary_goods": {
        "key": "primary_goods",
        "family": "iepg",
        "name_en": "Primary Goods",
        "name_es": "Bienes primarios",
        "table": "iepg_data.iepg_final_data",
        "column": "primary_goods"},
    "iepg_manufactures": {
        "key": "manufactures",
        "family": "iepg",
        "name_en": "Manufactures",
        "name_es": "Manufacturas",
        "table": "iepg_data.iepg_final_data",
        "column": "manufactures"},
    "iepg_services": {
        "key": "services",
        "family": "iepg",
        "name_en": "Services",
        "name_es": "Servicios",
        "table": "iepg_data.iepg_final_data",
        "column": "services"},
    "iepg_investments": {
        "key": "investments",
        "family": "iepg",
        "name_en": "Investments",
        "name_es": "Inversiones",
        "table": "iepg_data.iepg_final_data",
        "column": "investments"},
    "iepg_troops": {
        "key": "troops",
        "family": "iepg",
        "name_en": "Troops",
        "name_es": "Tropas",
        "table": "iepg_data.iepg_final_data",
        "column": "troops"},
    "iepg_military_equipment": {
        "key": "military_equipment",
        "family": "iepg",
        "name_en": "Military Equipment",
        "name_es": "Equipo militar",
        "table": "iepg_data.iepg_final_data",
        "column": "military_equipment"},
    "iepg_migrations": {
        "key": "migrations",
        "family": "iepg",
        "name_en": "Migrations",
        "name_es": "Migraciones",
        "table": "iepg_data.iepg_final_data",
        "column": "migrations"},
    "iepg_tourism": {
        "key": "tourism",
        "family": "iepg",
        "name_en": "Tourism",
        "name_es": "Turismo",
        "table": "iepg_data.iepg_final_data",
        "column": "tourism"},
    "iepg_sports": {
        "key": "sports",
        "family": "iepg",
        "name_en": "Sports",
        "name_es": "Deportes",
        "table": "iepg_data.iepg_final_data",
        "column": "sports"},
    "iepg_culture": {
        "key": "culture",
        "family": "iepg",
        "name_en": "Culture",
        "name_es": "Cultura",
        "table": "iepg_data.iepg_final_data",
        "column": "culture"},
    "iepg_information": {
        "key": "information",
        "family": "iepg",
        "name_en": "Information",
        "name_es": "Información",
        "table": "iepg_data.iepg_final_data",
        "column": "information"},
    "iepg_technology": {
        "key": "technology",
        "family": "iepg",
        "name_en": "Technology",
        "name_es": "Tecnología",
        "table": "iepg_data.iepg_final_data",
        "column": "technology"},
    "iepg_science": {
        "key": "science",
        "family": "iepg",
        "name_en": "Science",
        "name_es": "Ciencia",
        "table": "iepg_data.iepg_final_data",
        "column": "science"},
    "iepg_education": {
        "key": "education",
        "family": "iepg",
        "name_en": "Education",
        "name_es": "Educación",
        "table": "iepg_data.iepg_final_data",
        "column": "education"},
    "iepg_cooperation": {
        "key": "cooperation",
        "family": "iepg",
        "name_en": "Cooperation",
        "name_es": "Cooperación",
        "table": "iepg_data.iepg_final_data",
        "column": "cooperation"},
    "iepg_economic_presence": {
        "key": "economic_presence",
        "family": "iepg",
        "name_en": "Economic Presence",
        "name_es": "Presencia económica",
        "table": "iepg_data.iepg_final_data",
        "column": "economic_presence"},
    "iepg_military_presence": {
        "key": "military_presence",
        "family": "iepg",
        "name_en": "Military Presence",
        "name_es": "Presencia militar",
        "table": "iepg_data.iepg_final_data",
        "column": "military_presence"},
    "iepg_soft_presence": {
        "key": "soft_presence",
        "family": "iepg",
        "name_en": "Soft Presence",
        "name_es": "Presencia blanda",
        "table": "iepg_data.iepg_final_data",
        "column": "soft_presence"},
    "iepg": {
        "key": "iepg",
        "family": "iepg",
        "name_en": "IEPG",
        "name_es": "IEPG",
        "table": "iepg_data.iepg_final_data",
        "column": "iepg"},
    "iepe_energy": {
        "key": "energy",
        "family": "iepe",
        "name_en": "Energy",
        "name_es": "Energía",
        "table": "iepg_data.iepe_final_data",
        "column": "energy"},
    "iepe_primary_goods": {
        "key": "primary_goods",
        "family": "iepe",
        "name_en": "Primary Goods",
        "name_es": "Bienes primarios",
        "table": "iepg_data.iepe_final_data",
        "column": "primary_goods"},
    "iepe_manufactures": {
        "key": "manufactures",
        "family": "iepe",
        "name_en": "Manufactures",
        "name_es": "Manufacturas",
        "table": "iepg_data.iepe_final_data",
        "column": "manufactures"},
    "iepe_services": {
        "key": "services",
        "family": "iepe",
        "name_en": "Services",
        "name_es": "Servicios",
        "table": "iepg_data.iepe_final_data",
        "column": "services"},
    "iepe_investments": {
        "key": "investments",
        "family": "iepe",
        "name_en": "Investments",
        "name_es": "Inversiones",
        "table": "iepg_data.iepe_final_data",
        "column": "investments"},
    "iepe_troops": {
        "key": "troops",
        "family": "iepe",
        "name_en": "Troops",
        "name_es": "Tropas",
        "table": "iepg_data.iepe_final_data",
        "column": "troops"},
    "iepe_military_equipment": {
        "key": "military_equipment",
        "family": "iepe",
        "name_en": "Military Equipment",
        "name_es": "Equipo militar",
        "table": "iepg_data.iepe_final_data",
        "column": "military_equipment"},
    "iepe_migrations": {
        "key": "migrations",
        "family": "iepe",
        "name_en": "Migrations",
        "name_es": "Migraciones",
        "table": "iepg_data.iepe_final_data",
        "column": "migrations"},
    "iepe_tourism": {
        "key": "tourism",
        "family": "iepe",
        "name_en": "Tourism",
        "name_es": "Turismo",
        "table": "iepg_data.iepe_final_data",
        "column": "tourism"},
    "iepe_sports": {
        "key": "sports",
        "family": "iepe",
        "name_en": "Sports",
        "name_es": "Deportes",
        "table": "iepg_data.iepe_final_data",
        "column": "sports"},
    "iepe_culture": {
        "key": "culture",
        "family": "iepe",
        "name_en": "Culture",
        "name_es": "Cultura",
        "table": "iepg_data.iepe_final_data",
        "column": "culture"},
    "iepe_information": {
        "key": "information",
        "family": "iepe",
        "name_en": "Information",
        "name_es": "Información",
        "table": "iepg_data.iepe_final_data",
        "column": "information"},
    "iepe_technology": {
        "key": "technology",
        "family": "iepe",
        "name_en": "Technology",
        "name_es": "Tecnología",
        "table": "iepg_data.iepe_final_data",
        "column": "technology"},
    "iepe_science": {
        "key": "science",
        "family": "iepe",
        "name_en": "Science",
        "name_es": "Ciencia",
        "table": "iepg_data.iepe_final_data",
        "column": "science"},
    "iepe_education": {
        "key": "education",
        "family": "iepe",
        "name_en": "Education",
        "name_es": "Educación",
        "table": "iepg_data.iepe_final_data",
        "column": "education"},
    "iepe_cooperation": {
        "key": "cooperation",
        "family": "iepe",
        "name_en": "Cooperation",
        "name_es": "Cooperación",
        "table": "iepg_data.iepe_final_data",
        "column": "cooperation"},
    "iepe_economic_presence": {
        "key": "economic_presence",
        "family": "iepe",
        "name_en": "Economic Presence",
        "name_es": "Presencia económica",
        "table": "iepg_data.iepe_final_data",
        "column": "economic_presence"},
    "iepe_military_presence": {
        "key": "military_presence",
        "family": "iepe",
        "name_en": "Military Presence",
        "name_es": "Presencia militar",
        "table": "iepg_data.iepe_final_data",
        "column": "military_presence"},
    "iepe_soft_presence": {
        "key": "soft_presence",
        "family": "iepe",
        "name_en": "Soft Presence",
        "name_es": "Presencia blanda",
        "table": "iepg_data.iepe_final_data",
        "column": "soft_presence"},
    "iepe": {
        "key": "iepe",
        "family": "iepe",
        "name_en": "IEPE",
        "name_es": "IEPE",
        "table": "iepg_data.iepe_final_data",
        "column": "iepe"},
    "population": {
        "key": "population",
        "family": "context",
        "name_en": "Population",
        "name_es": "Población",
        "table": "iepg_data.pob_pib",
        "column": "population"},
    "gdp": {
        "key": "gdp",
        "family": "context",
        "name_en": "GDP",
        "name_es": "PIB",
        "table": "iepg_data.pob_pib",
        "column": "pib"}
}
