import org.junit.Rule;
import org.junit.Test;
import org.junit.contrib.java.lang.system.StandardOutputStreamLog;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

public class StandardOutputTest {
    @Rule
    public final StandardOutputStreamLog log = new StandardOutputStreamLog();

    @Test
    public void play() {
        System.out.println("hello");

        assertThat(log.getLog(), is("hello" + System.getProperty("line.separator")));
    }
}
