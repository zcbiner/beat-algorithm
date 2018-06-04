package stack;

import java.util.LinkedList;
import java.util.Queue;

public class 猫狗队列 {

    abstract static class Pet {
        private String type;

        public Pet(String type) {
            this.type = type;
        }

        public String getType() {
            return type;
        }
    }
    static class Cat extends Pet {

        public Cat() {
            super("猫");
        }
    }
    static class Dog extends Pet {

        public Dog(String type) {
            super("狗");
        }
    }

    /*****************解决方法*******************/

    static class PetWrapper {
        private Pet pet;
        private int count;

        public PetWrapper(Pet pet, int count) {
            this.pet = pet;
            this.count = count;
        }

        public Pet getPet() {
            return pet;
        }

        public int getCount() {
            return count;
        }

        public String getType() {
            return pet.getType();
        }
    }

    static class PetQueue {
        private Queue<PetWrapper> catQueue = new LinkedList<>();
        private Queue<PetWrapper> dogQueue = new LinkedList<>();
        private int count = 0;

        public void add(Pet pet) {
            PetWrapper petWrapper = new PetWrapper(pet, count++);
            if (pet.getType().equals("猫")) {
                catQueue.add(petWrapper);
            } else if (pet.getType().equals("狗")) {
                dogQueue.add(petWrapper);
            }
        }

        public Pet poll() {
            if (catQueue.isEmpty() && dogQueue.isEmpty()) {
                return null;
            }
            if (catQueue.isEmpty()) {
                return dogQueue.poll().getPet();
            }
            if (dogQueue.isEmpty()) {
                return catQueue.poll().getPet();
            }
            if (dogQueue.peek().getCount() < catQueue.peek().getCount()) {
                return dogQueue.poll().getPet();
            } else {
                return catQueue.poll().getPet();
            }
        }

        public Dog pollDog() {
            if (dogQueue.isEmpty()) {
                return null;
            }

            return (Dog) dogQueue.poll().getPet();
        }

        public Cat pollCat() {
            if (catQueue.isEmpty()) {
                return null;
            }

            return (Cat) catQueue.poll().getPet();
        }
    }
}
