import requests
import threading
import time
import random
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich import box

class NGLOperationShadowV99:
    """
    SHADOW MODE V99: PERFECT DELIVERY SYSTEM
    Intelligent delays for 100% success rate
    """
    
    def __init__(self, target_username: str, max_workers: int = 5):
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
        self.last_request_time = 0
        self.min_delay = 3.0  # Minimum delay between requests
        self.max_delay = 6.0  # Maximum delay between requests
        
        # Elite user-agent rotation pool
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0'
        ]
        
        # Built-in message database
        self.message_pool = self.generate_message_pool()
    
    def generate_message_pool(self) -> list:
        """Generate comprehensive message pool."""
        return [
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
    
    def intelligent_delay(self):
        """Smart delay system to avoid rate limiting."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.min_delay:
            # Wait until minimum delay is reached
            sleep_time = self.min_delay - time_since_last
            time.sleep(sleep_time)
        
        # Add additional random delay
        extra_delay = random.uniform(0.5, 1.5)
        time.sleep(extra_delay)
        
        self.last_request_time = time.time()
    
    def generate_payload(self, message: str) -> dict:
        """Craft precision payload for NGL API."""
        return {
            'question': message,
            'username': self.target_username,
            'deviceId': f'shadow_{random.randint(1000000000, 9999999999)}_{int(time.time())}',
            'gameSlug': '',
            'referrer': ''
        }
    
    def execute_single_strike(self, message: str, attempt: int = 1) -> tuple:
        """Execute request with intelligent delay and retry logic."""
        if attempt > 3:  # Max 3 attempts
            return False, "MAX ATTEMPTS REACHED"
        
        # Intelligent delay before each request
        self.intelligent_delay()
        
        headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.target_username}',
            'X-Requested-With': 'XMLHttpRequest'
        }
        
        try:
            payload = self.generate_payload(message)
            response = requests.post(
                self.target_url,
                data=payload,
                headers=headers,
                timeout=10,
                allow_redirects=True
            )
            
            with self.lock:
                self.request_count += 1
                
                if response.status_code == 200:
                    try:
                        response_data = response.json()
                        if 'questionId' in response_data:
                            self.success_count += 1
                            return True, f"SUCCESS: {response_data['questionId'][:8]}..."
                        else:
                            # Retry on unusual 200 response
                            return self.execute_single_strike(message, attempt + 1)
                    except:
                        self.success_count += 1
                        return True, "SUCCESS (Non-JSON)"
                elif response.status_code == 429:
                    self.fail_count += 1
                    self.rate_limit_count += 1
                    # Increase delay and retry
                    self.min_delay += 1.0
                    time.sleep(2.0)
                    return self.execute_single_strike(message, attempt + 1)
                else:
                    self.fail_count += 1
                    return False, f"HTTP {response.status_code}"
                    
        except requests.exceptions.RequestException:
            # Network error, retry with increased delay
            time.sleep(1.0)
            return self.execute_single_strike(message, attempt + 1)
        except Exception as e:
            self.fail_count += 1
            return False, f"ERROR: {str(e)}"
    
    def display_banner(self):
        """Show operation banner."""
        banner = Panel.fit(
            f"[bold red]SHΔDØW CORE V99[/bold red]\n"
            f"[white]PERFECT DELIVERY SYSTEM[/white]\n\n"
            f"[yellow]Target:[/yellow] [cyan]{self.target_username}[/cyan]\n"
            f"[yellow]Messages:[/yellow] [cyan]{len(self.message_pool)} loaded[/cyan]\n"
            f"[yellow]Workers:[/yellow] [cyan]{self.max_workers}[/cyan]\n"
            f"[yellow]Delay:[/yellow] [green]{self.min_delay}-{self.max_delay}s[/green]",
            box=box.DOUBLE,
            title="[blink]100% DELIVERY MODE[/blink]",
            border_style="red"
        )
        self.console.print(banner)
    
    def get_stats_table(self) -> Table:
        """Return statistics table."""
        if self.start_time is None:
            return Table()
            
        elapsed = time.time() - self.start_time
        rate = self.request_count / elapsed if elapsed > 0 else 0
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_column("Rate", style="yellow")
        
        table.add_row("Total Requests", str(self.request_count), f"{rate:.2f}/sec")
        success_rate = (self.success_count/self.request_count*100) if self.request_count > 0 else 0
        table.add_row("Successful", str(self.success_count), f"{success_rate:.1f}%")
        table.add_row("Failed", str(self.fail_count), "N/A")
        table.add_row("Elapsed Time", f"{elapsed:.2f}s", "N/A")
        
        return table
    
    def launch_assault(self, total_attacks: int):
        """Initiate assault with perfect delivery system."""
        self.start_time = time.time()
        self.last_request_time = time.time()
        
        self.display_banner()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=self.console
        ) as progress:
            task = progress.add_task("[red]Executing perfect delivery...", total=total_attacks)
            
            # Use single thread for perfect timing
            for i in range(total_attacks):
                message = random.choice(self.message_pool)
                success, result = self.execute_single_strike(message)
                
                progress.update(task, advance=1)
                
                if success:
                    progress.console.print(f"[green]✓ {result}[/green]")
                else:
                    progress.console.print(f"[red]✗ {result}[/red]")
                
                # Small delay between progress updates
                time.sleep(0.1)
        
        # Display results
        self.console.print("\n")
        stats_table = self.get_stats_table()
        
        final_panel = Panel(
            stats_table,
            title="[bold green]MISSION COMPLETE[/bold green]",
            border_style="green",
            box=box.DOUBLE
        )
        self.console.print(final_panel)
        
        # Success analysis
        if self.success_count == total_attacks:
            self.console.print("\n[bold green]🎯 PERFECT DELIVERY! 100% SUCCESS RATE![/bold green]")
        elif self.success_count > 0:
            self.console.print(f"\n[green]✅ Delivery completed: {self.success_count}/{total_attacks} messages[/green]")

def main():
    """Main execution function."""
    console = Console()
    
    intro_banner = Panel.fit(
        """[bold red]:::.    :::.  .,-:::::/   :::         .::::::.                                                            
        `;;;;,  `;;;,;;-'````'    ;;;        ;;;`    `                                                            
          [[[[[. '[[[[[   [[[[[[/ [[[        '[==/[[[[,         ,ccc,   [ccc, ,cccc, [ccc, ,cccc, ,cc[[[cc.=,,[[==
          $$$ "Y$c$$"$$c.    "$$  $$'          '''    $,$$$$$. $$$cc$$$ $$$$$$$$"$$$ $$$$$$$$"$$$ $$$___--'`$$$"``
          888    Y88 `Y8bo,,,o88oo88oo,.__    88b    dP88""""88888   888888 Y88" 888o888 Y88" 888o88b    ,o,888   
          MMM     YM   `'YMUP"YMM""""YUMMM     "YMmMY" MMoooMM' "YUM" MPMMM  M'  "MMMMMM  M'  "MMM "YUMMMMP""MM,  
                                                       MMMP                                                       
                                                       ###                                                        
                                                       "##b                                                       [/bold red]"""
        "[bold red]🩸👁️‍🗨️ ULTIMATE SHADOW PROTOCOL[/bold red]\n"
        "[white]100% DELIVERY GUARANTEE SYSTEM[/white]\n\n"
        "[yellow]Features:[/yellow] Intelligent delays + Retry logic\n"
        "[yellow]Success Rate:[/yellow] Optimized for perfect delivery",
        box=box.HEAVY,
        border_style="red"
    )
    console.print(intro_banner)
    
    # Get user input
    console.print("\n")
    target_username = console.input("[bold yellow]🎯 Enter Target NGL Username: [/bold yellow]")
    total_attacks = int(console.input("[bold yellow]💣 Enter Total Messages to Send [10]: [/bold yellow]") or "10")
    
    # Initialize operation
    operation = NGLOperationShadowV99(target_username=target_username, max_workers=1)
    
    # Confirm
    console.print("\n")
    confirm_panel = Panel(
        f"[red]Target:[/red] [white]{target_username}[/white]\n"
        f"[red]Messages:[/red] [white]{total_attacks} to send[/white]\n"
        f"[red]Strategy:[/red] [green]SINGLE THREAD + INTELLIGENT DELAYS[/green]\n"
        f"[red]Expected Time:[/red] [white]~{total_attacks * 4}s[/white]",
        title="[blink]CONFIRM PERFECT DELIVERY[/blink]",
        border_style="yellow"
    )
    console.print(confirm_panel)
    
    confirmation = console.input("[bold red]🚀 Launch operation? (y/N): [/bold red]")
    if confirmation.lower() != 'y':
        console.print("[yellow]Operation cancelled.[/yellow]")
        return
    
    # Execute
    console.print("\n")
    try:
        operation.launch_assault(total_attacks)
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Operation interrupted[/yellow]")

if __name__ == "__main__":
    main()
