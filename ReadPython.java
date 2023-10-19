import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReadPython {

    public static void main(String[] args) throws IOException, InterruptedException {

        String path = "C:\\Users\\omert\\Task\\Design-Patterns\\Structural Design Patterns\\Flyweight.py";
        

        ProcessBuilder pb = new ProcessBuilder("python", path).inheritIO();
        Process process = pb.start();
        process.waitFor();
        BufferedReader bfr = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line = "";
        while ((line = bfr.readLine()) != null) {
            System.out.println(line);
        }
    }
}
