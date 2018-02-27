import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public


class Book {
public static void main(String[] args) throws InterruptedException {
// TODO Auto-generated method stub
System.setProperty("webdriver.gecko.driver", "E:\\Automation\\sagar\\geckodriver.exe");
WebDriver driver = new FirefoxDriver();
driver.get("http://nepalinn.com/search/result");

Thread.sleep(5000);

driver.findElement(By.xpath("//*[@name = 'submit_search']")).click();

Thread.sleep(4000);

WebElement text1 = driver.findElement(By.xpath(".//*[text()='Hotel New Solitary Lodge']"));

String text2 = driver.findElement(By.xpath(".//*[text()='Hotel New Solitary Lodge']")).getText();
System.out.println(text2);
String Hotel_name = "HOTEL NEW SOLITARY LODGE";
if (text2.equals(Hotel_name))
{

driver.findElement(By.xpath("//*[@href= 'http://nepalinn.com/hotel_new_solitary_lodge']//button[text()='Book']")).click();

}

}
}