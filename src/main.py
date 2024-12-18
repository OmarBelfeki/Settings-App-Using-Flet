import flet as ft


class Main:
    def __init__(self, page: ft.Page) -> None:
        self.page = page


        self.page.title = "Settings Page"
        self.page.bgcolor = ft.Colors.WHITE
        self.page.padding = 0
        self.page.update()

        self.page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.Colors.WHITE,
            elevation=7,
            shadow_color=ft.Colors.BLACK,
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.HOME_OUTLINED,
                        icon_color="#4B4B4B",
                        icon_size=22.67*1.6,
                        style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)
                    ),
                    ft.IconButton(
                        icon=ft.Icons.SEARCH_OUTLINED,
                        icon_color="#4B4B4B",
                        icon_size=22.67 * 1.6,
                        style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)
                    ),
                    ft.Container(
                        width=32, height=32,
                        border=ft.border.all(width=3, color="#4B4B4B"),
                        alignment=ft.alignment.center,
                        content=ft.Icon(
                            name=ft.Icons.ADD,
                            color="#4B4B4B",
                            size=25
                        ),
                        on_click=lambda e: e.page.open(
                            ft.BottomSheet(
                                content=ft.Container(
                                    alignment=ft.alignment.center,
                                    content=ft.Text(value="By Omar Belfeki", size=30)
                                )
                            )
                        )
                    ),
                    ft.IconButton(
                        icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                        icon_color="#4B4B4B",
                        icon_size=22.67 * 1.6,
                        style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.SETTINGS,
                                icon_color=ft.Colors.BLACK,
                                icon_size=22.67 * 1.6,
                                style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)
                            ),
                            ft.Icon(
                                name=ft.Icons.CIRCLE,
                                color="#E5386D",
                                size=6*1.6,
                                offset=ft.Offset(x=0, y=-1.9)
                            )
                        ]
                    )
                ]
            )
        )

        self.page.add(
            ft.Stack(
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor="#E5386D",
                        width=self.page.width, height=294,
                        border_radius=ft.border_radius.only(bottom_left=12, bottom_right=12),
                        alignment=ft.alignment.top_center,
                        padding=ft.padding.only(left=16, top=40),
                        content=ft.Row(
                            controls=[
                                ft.Icon(
                                    name=ft.Icons.SETTINGS,
                                    color=ft.Colors.WHITE,
                                    size=40
                                ),
                                ft.Text(
                                    value="Settings",
                                    color=ft.Colors.WHITE,
                                    size=30,
                                    font_family="Rubik",
                                    weight=ft.FontWeight.BOLD,
                                    style=ft.TextStyle(letter_spacing=3.5)
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.WHITE,
                        width=self.page.width - 16 * 2, height=911,
                        # border=ft.border.all(width=1, color="blue"),
                        top=128, left=16,
                        border_radius=ft.border_radius.only(top_left=16, top_right=16),
                        shadow=ft.BoxShadow(
                            blur_radius=11,
                            offset=ft.Offset(x=0, y=2),
                            color=ft.Colors.with_opacity(opacity=0.35, color="4B4B4B")
                        ),
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            height=3,
                            width=self.page.width - 16 * 2,
                            controls=[
                                ft.Divider(height=24, color=ft.Colors.TRANSPARENT),
                                ft.Row(
                                    controls=[
                                        ft.VerticalDivider(width=13, color=ft.Colors.TRANSPARENT),
                                        ft.CircleAvatar(
                                            bgcolor="red",
                                            height=40, width=40,
                                            foreground_image_src="Omar Belfeki.jpg"
                                        ),
                                        ft.Text(
                                            value="Omar Belfeki",
                                            color=ft.Colors.BLACK,
                                            size=18,
                                            font_family="Rubik",
                                            weight=ft.FontWeight.BOLD
                                        )
                                    ]
                                ),
                                ft.Divider(color="#CACACA"),
                                ft.Container(
                                    padding=ft.padding.only(left=25, right=25, top=7, bottom=-25),
                                    content=ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(
                                                value="Account Settings",
                                                size=18,
                                                color="#ADADAD"
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                    controls=[
                                                        ft.Text(
                                                            value="Edit profile",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Icon(
                                                            name=ft.Icons.ARROW_FORWARD_IOS_SHARP,
                                                            color="#4B4B4B"
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                    controls=[
                                                        ft.Text(
                                                            value="Changer password",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Icon(
                                                            name=ft.Icons.ARROW_FORWARD_IOS_SHARP,
                                                            color="#4B4B4B"
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                    controls=[
                                                        ft.Text(
                                                            value="Add a payment method",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Icon(
                                                            name=ft.Icons.ADD,
                                                            color="#4B4B4B",
                                                            size=30
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            value="Push notification",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Switch(
                                                            value=True,
                                                            active_color=ft.Colors.WHITE,
                                                            active_track_color="#E5386D",
                                                            inactive_track_color="#EAEAEA"
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            value="Dark mode",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Switch(
                                                            active_color=ft.Colors.WHITE,
                                                            active_track_color="#E5386D",
                                                            inactive_track_color="#EAEAEA"
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            ),
                                        ]
                                    )
                                ),
                                ft.Divider(color="#CACACA", height=15),
                                ft.Container(
                                    padding=ft.padding.only(left=25, right=25, top=7, bottom=-45),
                                    content=ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(
                                                value="More",
                                                size=18,
                                                color="#ADADAD"
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                    controls=[
                                                        ft.Text(
                                                            value="About us",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Icon(
                                                            name=ft.Icons.ARROW_FORWARD_IOS_SHARP,
                                                            color="#4B4B4B"
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            ),
                                            ft.TextButton(
                                                offset=ft.Offset(x=-0.02, y=0),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                    controls=[
                                                        ft.Text(
                                                            value="Privacy policy",
                                                            color=ft.Colors.BLACK,
                                                            size=18,
                                                            weight=ft.FontWeight.BOLD
                                                        ),
                                                        ft.Icon(
                                                            name=ft.Icons.ARROW_FORWARD_IOS_SHARP,
                                                            color="#4B4B4B"
                                                        )
                                                    ]
                                                ),
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.TRANSPARENT
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )



ft.app(target=Main, assets_dir="assets")
