nav = [
    {"link": "", "name": "Dashboard", "icon": "bx bx-grid-alt", "children": []},
    {
        "link": "#",
        "name": "Contacts",
        "icon": "bx bx-collection",
        "children": [
            {"link": "#", "name": "Contacts", "icon": None, "children": []},
            {
                "link": "customers/",
                "name": "Customers",
                "icon": "bx bx-user",
                "children": []
            },
            {
                "link": "suppliers/",
                "name": "Suppliers",
                "icon": "bx bx-download",
                "children": []
            }
        ]
    },
    {
        "link": "#",
        "name": "Inventory",
        "icon": "bx bx-hdd",
        "children": [
            {"link": "#", "name": "Inventory", "icon": None, "children": []},
            {
                "url": "item_list",
                "name": "Items",
                "icon": "bx bx-hdd",
                "children": []
            },
            {
                "url": "item_kits",
                "name": "Item kits",
                "icon": "bx bx-server",
                "children": []
            },
            {
                "url": "categories",
                "name": "Categories",
                "icon": "bx bx-folder",
                "children": []
            },
            {
                "link": "manufacturers",
                "name": "Manufacturers",
                "icon": "bx bx-notepad",
                "children": []
            },
            {
                "link": "modifiers",
                "name": "Modifiers",
                "icon": "bx bx-spreadsheet",
                "children": []
            },
            {"link": "tags", "name": "Tags", "icon": "bx bx-tag", "children": []},
            {
                "link": "attributes",
                "name": "Attributes",
                "icon": "bx bx-toggle-left",
                "children": []
            },
            {
                "link": "price_rules",
                "name": "Price Rules",
                "icon": "bx bx-purchase-tag",
                "children": []
            }
        ]
    },
    {
        "link": "reports/",
        "name": "Reports",
        "icon": "bx bx-bar-chart-alt",
        "children": []
    },
    {
        "link": "receiving/",
        "name": "Receiving",
        "icon": "bx bx-cloud-download",
        "children": []
    },
    {
        "link": "sales/",
        "name": "Sales",
        "icon": "bx bx-cart-alt",
        "children": []
    },
    {
        "link": "deliveries/",
        "name": "Deliveries",
        "icon": "bx bx-car",
        "children": []
    },
    {
        "link": "workorders/",
        "name": "Work Orders",
        "icon": "bx bx-list-check",
        "children": []
    },
    {
        "link": "expenses/",
        "name": "Expenses",
        "icon": "bx bx-money",
        "children": []
    },
    {
        "link": "appointments/",
        "name": "Apointments",
        "icon": "bx bx-calendar-alt",
        "children": []
    },
    {
        "link": "employees/",
        "name": "Employees",
        "icon": "bx bx-id-card",
        "children": []
    },
    {
        "link": "gift_cards",
        "name": "Gift Cards",
        "icon": "fa-solid fa-gifts",
        "children": []
    },
    {
        "link": "store_config",
        "name": "Store Config",
        "icon": "bx bx-cog",
        "children": []
    },
    {
        "link": "#",
        "name": "Invoices",
        "icon": "bx bx-receipt",
        "children": [
            {"link": "#", "name": "Invoices", "icon": None, "children": []},
            {
                "link": "invoices/invoices/customers",
                "name": "Customers",
                "icon": "bx bx-user",
                "children": []
            },
            {
                "link": "invoices/invoices/suppliers",
                "name": "Suppliers",
                "icon": "bx bx-download",
                "children": []
            }
        ]
    },
    {
        "link": "locations/",
        "name": "Locations",
        "icon": "bx bx-home",
        "children": []
    },
    {
        "link": "messages",
        "name": "Messages",
        "icon": "bx bx-chat",
        "children": []
    },
    {
        "link": "time_clock",
        "name": "Time Clock",
        "icon": "fa-solid fa-stopwatch",
        "children": []
    },
    {
        "link": "#",
        "name": "Log Out",
        "icon": "bx bx-power-off",
        "children": [
            {"link": "#", "name": "Log Out", "icon": None, "children": []}
        ]
    }
]


def links_renderer(request):
    return {"links": nav}
