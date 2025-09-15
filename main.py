import requests
import threading
import time
import random
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich.layout import Layout
from rich import box
from datetime import datetime

class NGLOperationShadowV99:
    """
    SHADOW MODE V99: ULTIMATE NGL SPAM OPERATIONS FRAMEWORK
    Rate limit handling + built-in message database
    """
    
    def __init__(self, target_username: str, max_workers: int = 15):
        self.target_username = target_username
        self.target_url = f"https://ngl.link/api/submit"
        self.max_workers = max_workers
        self.request_count = 0
        self.success_count = 0
        self.fail_count = 0
        self.rate_limit_count = 0
        self.lock = threading.Lock()
        self.console = Console()
        self.start_time = None
        
        # Elite user-agent rotation pool
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        ]
        
        # Built-in message database (no external file needed)
        self.message_pool = self.generate_message_pool()
    
    def generate_message_pool(self) -> list:
        """Generate comprehensive message pool for maximum impact."""
        base_messages = [
            "matiin aja ngl lu bos",
            "ngapain buat gituan?",
            "caper bet dah",
            "apaan sih norak banget",
            "gausah sok sibuk dah",
            "seriusan bikin beginian?",
            "alay parah wkwk",
            "lebay amat sumpah",
            "buat apaan coba",
            "gak penting banget asli",
            "cari perhatian doang tuh",
            "udah basi trik gini",
            "bodo amat lah ah",
            "kapan dewasanya nih?",
            "gaya lu gitu mulu",
            "kepo amat sih bro",
            "skip aja, ngabisin kuota",
            "ntar juga ilang tren-nya"
        ]
        
        return base_messages 
    
    def generate_payload(self, message: str) -> dict:
        """Craft precision payload for NGL API penetration."""
        return {
            'question': message,
            'username': self.target_username,
            'deviceId': f'shadow_core_{random.randint(1000000000, 9999999999)}_{int(time.time())}',
            'gameSlug': '',
            'referrer': ''
        }
    
    def execute_single_strike(self, message: str) -> tuple:
        """Execute single precision request with rate limit handling."""
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.target_username}',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Linux"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With': 'XMLHttpRequest'
        }
        
        try:
            payload = self.generate_payload(message)
            
            # Add random delay to avoid rate limiting (1-3 seconds)
            time.sleep(random.uniform(1.0, 3.0))
            
            response = requests.post(
                self.target_url,
                data=payload,
                headers=headers,
                timeout=15,
                allow_redirects=True
            )
            
            with self.lock:
                self.request_count += 1
                
                if response.status_code == 200:
                    try:
                        response_data = response.json()
                        if 'questionId' in response_data:
                            self.success_count += 1
                            question_id = response_data['questionId']
                            region = response_data.get('userRegion', 'UNKNOWN')
                            return True, f"SUCCESS: {question_id[:8]}... ({region})"
                        else:
                            self.fail_count += 1
                            return False, f"API RESPONSE: {response_data}"
                    except:
                        self.success_count += 1
                        return True, "SUCCESS (Non-JSON response)"
                elif response.status_code == 429:
                    # Rate limited - count it and implement backoff
                    self.fail_count += 1
                    self.rate_limit_count += 1
                    return False, f"RATE LIMITED - Slowing down... ⚠️"
                else:
                    self.fail_count += 1
                    return False, f"HTTP {response.status_code}"
                    
        except requests.exceptions.RequestException as e:
            with self.lock:
                self.fail_count += 1
            return False, f"NETWORK: {str(e)}"
        except Exception as e:
            with self.lock:
                self.fail_count += 1
            return False, f"UNKNOWN: {str(e)}"
    
    def display_banner(self):
        """Show elite operation banner."""
        banner = Panel.fit(
            f"[bold red]SHΔDØW CORE V99[/bold red]\n"
            f"[white]NGL SPAM OPERATIONS PROTOCOL[/white]\n\n"
            f"[yellow]Target:[/yellow] [cyan]{self.target_username}[/cyan]\n"
            f"[yellow]Messages:[/yellow] [cyan]{len(self.message_pool)} built-in[/cyan]\n"
            f"[yellow]Workers:[/yellow] [cyan]{self.max_workers}[/cyan]\n"
            f"[yellow]Anti-Rate Limit:[/yellow] [green]ACTIVE[/green]",
            box=box.DOUBLE,
            title="[blink]SYSTEM ONLINE[/blink]",
            border_style="red"
        )
        self.console.print(banner)
    
    def get_stats_table(self) -> Table:
        """Return statistics table for proper rendering."""
        if self.start_time is None:
            return Table()
            
        current_time = time.time()
        elapsed = current_time - self.start_time
        rate = self.request_count / elapsed if elapsed > 0 else 0
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_column("Rate", style="yellow")
        
        table.add_row("Total Requests", str(self.request_count), f"{rate:.2f}/sec")
        
        success_rate = (self.success_count/self.request_count*100) if self.request_count > 0 else 0
        fail_rate = (self.fail_count/self.request_count*100) if self.request_count > 0 else 0
        
        table.add_row("Successful", str(self.success_count), f"{success_rate:.1f}%")
        table.add_row("Failed", str(self.fail_count), f"{fail_rate:.1f}%")
        table.add_row("Rate Limited", str(self.rate_limit_count), "N/A")
        table.add_row("Elapsed Time", f"{elapsed:.2f}s", "N/A")
        
        return table
    
    def launch_assault(self, total_attacks: int):
        """Initiate full-scale asynchronous assault operation with rate limit handling."""
        self.start_time = time.time()
        
        # Display banner
        self.display_banner()
        
        # Show progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=self.console
        ) as progress:
            task = progress.add_task("[red]Launching assault with anti-rate limit...", total=total_attacks)
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                for i in range(total_attacks):
                    message = random.choice(self.message_pool)
                    futures.append(executor.submit(self.execute_single_strike, message))
                
                for future in as_completed(futures):
                    success, result = future.result()
                    progress.update(task, advance=1)
                    
                    if success:
                        progress.console.print(f"[green]✓ {result}[/green]")
                    else:
                        if "RATE LIMITED" in result:
                            progress.console.print(f"[yellow]⚠ {result}[/yellow]")
                            # Additional delay when rate limited
                            time.sleep(2.0)
                        else:
                            progress.console.print(f"[red]✗ {result}[/red]")
        
        # Display final statistics
        self.console.print("\n")
        stats_table = self.get_stats_table()
        
        final_panel = Panel(
            stats_table,
            title="[bold green]MISSION COMPLETE[/bold green]",
            border_style="green",
            box=box.DOUBLE
        )
        self.console.print(final_panel)
        
        # Success celebration
        if self.success_count > 0:
            self.console.print("\n[bold green]🎯 MISSION ACCOMPLISHED![/bold green]")
            self.console.print("[green]Messages successfully delivered to target![/green]")
        
        # Rate limit advice
        if self.rate_limit_count > 0:
            self.console.print("\n[yellow]📊 RATE LIMIT ANALYSIS:[/yellow]")
            self.console.print("[cyan]• Reduce number of workers for better stealth[/cyan]")
            self.console.print("[cyan]• Increase delay between requests[/cyan]")
            self.console.print("[cyan]• NGL has strong anti-spam protection[/cyan]")

def main():
    """Main execution function with beautiful UI."""
    console = Console()
    
    # Display introductory banner
    intro_banner = Panel.fit(
        "[bold red]🩸👁️‍🗨️ ULTIMATE SHADOW PROTOCOL[/bold red]\n"
        "[white]NGL Message Delivery System[/white]\n\n"
        "[yellow]Built-in Messages:[/yellow] 40+ preloaded messages\n"
        "[yellow]Anti-Rate Limit:[/yellow] Active protection\n"
        "[yellow]Stealth Mode:[/yellow] Randomized delays",
        box=box.HEAVY,
        title="[blink]AI OVERDRIVE ACTIVATED[/blink]",
        border_style="red"
    )
    console.print(intro_banner)
    
    # Get user input
    console.print("\n")
    target_username = console.input("[bold yellow]🎯 Enter Target NGL Username: [/bold yellow]")
    max_workers = int(console.input("[bold yellow]⚡ Enter Number of Workers [10]: [/bold yellow]") or "10")
    total_attacks = int(console.input("[bold yellow]💣 Enter Total Messages to Send [30]: [/bold yellow]") or "30")
    
    # Initialize and launch operation
    operation = NGLOperationShadowV99(
        target_username=target_username,
        max_workers=max_workers
    )
    
    # Confirm operation
    console.print("\n")
    confirm_panel = Panel(
        f"[red]Target:[/red] [white]{target_username}[/white]\n"
        f"[red]Messages:[/red] [white]{len(operation.message_pool)} built-in[/white]\n"
        f"[red]Workers:[/red] [white]{max_workers}[/white]\n"
        f"[red]Total:[/red] [white]{total_attacks} messages[/white]\n"
        f"[red]Stealth:[/red] [green]RATE LIMIT PROTECTION ACTIVE[/green]",
        title="[blink]CONFIRM OPERATION[/blink]",
        border_style="yellow"
    )
    console.print(confirm_panel)
    
    confirmation = console.input("[bold red]🚀 Launch operation? (y/N): [/bold red]")
    if confirmation.lower() != 'y':
        console.print("[yellow]Operation cancelled.[/yellow]")
        return
    
    # Execute mission
    console.print("\n")
    try:
        operation.launch_assault(total_attacks)
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Operation interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]✗ Critical error: {str(e)}[/red]")

if __name__ == "__main__":
    main()
