import flet as ft
from ollama import Client

class MessageBubble(ft.Row):
    def __init__(self, sender, text):
        super().__init__()
        self.is_user = sender == "You"
        bg_color = ft.Colors.BLUE_GREY_900 if self.is_user else ft.Colors.TRANSPARENT
        text_color = ft.Colors.WHITE if self.is_user else ft.Colors.WHITE70
        avatar_color = ft.Colors.PURPLE_400 if self.is_user else ft.Colors.BLUE_400
        avatar_text = "U" if self.is_user else "G"
        
        avatar = ft.CircleAvatar(
            content=ft.Text(avatar_text, color=ft.Colors.WHITE),
            bgcolor=avatar_color,
        )
        
        if self.is_user:
            self.text_view = ft.Text(text, color=text_color, selectable=True)
            content = self.text_view
        else:
            self.text_view = ft.Markdown(text, selectable=True, extension_set=ft.MarkdownExtensionSet.GITHUB_WEB)
            
            async def copy_clicked(e):
                await ft.Clipboard().set(self.text_view.value.strip())
                copy_button.icon = ft.Icons.CHECK
                copy_button.icon_color = ft.Colors.GREEN
                copy_button.tooltip = "已複製！"
                copy_button.update()
                
            copy_button = ft.IconButton(
                icon=ft.Icons.CONTENT_COPY,
                icon_size=16,
                tooltip="複製內容 (包含格式)",
                on_click=copy_clicked,
                icon_color=ft.Colors.WHITE54,
            )
            
            content = ft.Column([
                self.text_view,
                ft.Row([copy_button], alignment=ft.MainAxisAlignment.END, spacing=0)
            ], tight=True, spacing=5)
            
        container = ft.Container(
            content=content,
            bgcolor=bg_color,
            border_radius=15,
            padding=10,
            expand=True,
        )
        
        self.controls = [container, avatar] if self.is_user else [avatar, container]
        self.alignment = ft.MainAxisAlignment.END if self.is_user else ft.MainAxisAlignment.START
        self.vertical_alignment = ft.CrossAxisAlignment.START

def main(page: ft.Page):
    page.title = "CallGemma 4 - v1.0.2"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 900
    page.window_height = 800
    page.padding = 20

    client = Client()
    conversation_history = []

    chat_view = ft.ListView(
        expand=True,
        spacing=15,
        auto_scroll=True,
        padding=20,
    )

    def send_message_click(e):
        user_text = user_input.value
        if not user_text.strip():
            return
        
        chat_view.controls.append(MessageBubble("You", user_text))
        conversation_history.append({'role': 'user', 'content': user_text})
        
        user_input.value = ""
        user_input.disabled = True
        send_button.disabled = True
        
        # Add empty bot message bubble AND loading state below it
        bot_bubble = MessageBubble("Gemma", "")
        chat_view.controls.append(bot_bubble)
        
        loading_row = ft.Row([
            ft.ProgressRing(width=20, height=20, stroke_width=2, color=ft.Colors.BLUE_400),
            ft.Text(" Gemma 正在生成回應中...", color=ft.Colors.WHITE70, italic=True)
        ], alignment=ft.MainAxisAlignment.START)
        chat_view.controls.append(loading_row)
        
        page.update()

        import threading
        def process_ollama():
            try:
                response = client.chat(model='gemma4:latest', messages=conversation_history, stream=True)
                bot_text = ""
                for chunk in response:
                    bot_text += chunk['message']['content']
                    bot_bubble.text_view.value = bot_text
                    page.update()
                    
                conversation_history.append({'role': 'assistant', 'content': bot_text})
            except Exception as ex:
                bot_bubble.text_view.value = f"**Error connecting to Gemma:**\n\n```\n{ex}\n```"
            
            if loading_row in chat_view.controls:
                chat_view.controls.remove(loading_row)
                
            user_input.disabled = False
            send_button.disabled = False
            page.update()
            
        page.run_thread(process_ollama)

    user_input = ft.TextField(
        hint_text="Ask Gemma anything...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
        border_radius=20,
    )

    send_button = ft.IconButton(
        icon=ft.Icons.SEND_ROUNDED,
        tooltip="Send message",
        on_click=send_message_click,
        icon_color=ft.Colors.BLUE_400,
    )

    input_row = ft.Container(
        content=ft.Row([user_input, send_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.END),
        padding=10,
    )

    page.add(
        ft.Container(
            content=chat_view, 
            expand=True, 
            border=ft.Border.all(1, "outline"), 
            border_radius=15,
            bgcolor="background"
        ),
        input_row
    )

ft.run(main)
